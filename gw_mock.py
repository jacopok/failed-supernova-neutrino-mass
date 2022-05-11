import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
import astropy.units as u

import scipy.signal as signal

from pycbc.psd import from_string as psd_from_string
from pycbc.noise import noise_from_psd
from pycbc.psd import interpolate
from pycbc.filter.resample import highpass, lowpass

from scipy.io.wavfile import write
from scipy.signal.windows import get_window


def make_wavable(array):
    """Make a numpy array ready to be saved as a WAV file.
    This entails turning it into integers, normalizing them 
    to their highest attainable value.
    """
    return (array / array.max() * np.iinfo(np.int16).max).astype(np.int16)


def read_file_and_resample(filename: str, sample_rate: int, distance: u.Quantity[u.kpc]):

    scaling = (distance / u.cm).to(u.dimensionless_unscaled).value
    # this is D times h+, in centimeters

    data = pd.read_csv(filename, sep=' ', names=['time', 'hplus', 'hcross'], skiprows=1)

    data['time'] -= min(data['time'])
    total_time = max(data['time'])
    time = np.linspace(0, total_time, num=int(total_time*sample_rate))
    delta_t = time[1] - time[0]
    hplus = np.interp(time, data['time'], data['hplus']) / scaling
    
    return time, hplus

def set_to_zero_after_time(time_stop: float, time_array: np.ndarray, waveform: np.ndarray):
    
    index_stop = np.searchsorted(time_array, time_stop)

    transition_steps = 1

    waveform[index_stop-transition_steps:index_stop] *= (np.arange(transition_steps, 0, step=-1) / transition_steps)**3
    waveform[index_stop:] = 0
    
    return waveform

def add_noise_and_whiten(waveform: np.ndarray, srate: int, seglen: float):
    """Inspired from https://pycbc.org/pycbc/latest/html/gw150914.html#plotting-the-whitened-strain
    """

    delta_f = 1 / seglen
    low_frequency_cutoff=1

    my_psd = psd_from_string(
        'EinsteinTelescopeP1600143', 
        int(srate / 2 / delta_f)+1, 
        delta_f, 
        low_frequency_cutoff,
    )

    for i, element in enumerate(my_psd):
        if element < 1e-50:
            my_psd[i] = 1e-30

    noise = noise_from_psd(len(waveform), 1/srate, my_psd)

    waveform += noise
    # waveform = noise
    
    window = get_window(('tukey', .1), len(waveform))
    
    waveform *= window

    waveform = waveform.to_frequencyseries()

    # return waveform
    # my_psd = interpolate(my_psd, waveform.to_frequencyseries().delta_f) + 1e-60

    whitened = waveform / np.sqrt(my_psd / 2 / seglen)
    
    lowpassed = lowpass(whitened.to_timeseries(), 3000)
    bandpassed = highpass(lowpassed, 100)
    
    return bandpassed

def analyze(times, waveform):
    width = .001
    
    results = []
    for t in times:
        window = np.heaviside(times - t - width, 0) - np.heaviside(times - t + width, 0)
        filtered = window * waveform
        results.append(np.std(filtered))
        
    return np.array(results)

def main():

    TIME_STOP = 0.32
    SRATE = 2**14
    waveform_file = 'GW_strains/s60.0.swbj15.horo.3d.gw.dat'
    distance = 1. * u.kpc

    time, hplus = read_file_and_resample(waveform_file, SRATE, distance)
    hplus = set_to_zero_after_time(TIME_STOP, time, hplus)
    delta_t = time[1] - time[0]
    
    hplus = add_noise_and_whiten(hplus, SRATE, len(hplus) / SRATE)
    
    # hplus_fd = hplus.to_frequencyseries()
    
    # plt.plot(hplus_fd.sample_frequencies, abs(hplus_fd))
    # seglen=len(hplus) / SRATE
    # delta_f = 1 / seglen
    # low_frequency_cutoff=1
    # my_psd = psd_from_string(
    #     'EinsteinTelescopeP1600143', 
    #     int(SRATE / 2 / delta_f)+1, 
    #     delta_f, 
    #     low_frequency_cutoff,
    # )
    # plt.plot(my_psd.sample_frequencies, abs(np.sqrt(my_psd.to_frequencyseries())))
    # plt.show()
    
    # plt.plot(abs(hplus.to_frequencyseries()))
    # plt.show()

    f, t, Sxx = signal.spectrogram(hplus, 1/delta_t, nperseg=1<<8)
    plt.pcolormesh(
        t, f[:30], Sxx[:30, :], 
        shading='gouraud', 
        norm=mpl.colors.PowerNorm(gamma=.4)
    )
    plt.title(f'ET sensitivity, distance={distance}')
    plt.savefig(f'spectrum_{distance.value}kpc.pdf')
    plt.close()

    # f, t, Sxx = signal.spectrogram(hplus, 1/delta_t, nperseg=1<<6)
    # plt.pcolormesh(
    #     t, f[:25], Sxx[:25], 
    #     shading='gouraud', 
    #     norm=mpl.colors.PowerNorm(gamma=.3)
    # )
    # plt.ylim(0, 2e4)
    # plt.xlim(.498, .502)
    # plt.show()

    results = analyze(time[:-1], hplus)
    # plt.plot((time[:-1]-TIME_STOP)*1000, results*10)
    plt.plot((time[:-1]-TIME_STOP)*1000, hplus)
    plt.xlim(-100, 100)
    plt.xlabel('Time from end of signal [ms]')
    plt.title(f'ET sensitivity, distance={distance}')
    plt.savefig(f'signal_{distance.value}kpc.pdf')
    plt.show()
    plt.close()
    
if __name__ == '__main__':
    main()