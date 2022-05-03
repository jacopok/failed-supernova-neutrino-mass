#%%

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
import astropy.units as u

import scipy.signal as signal

from pycbc.psd import from_string as psd_from_string
from pycbc.noise import noise_from_psd

TIME_STOP = 0.5
distance = .5 * u.kpc
scaling = (distance / u.cm).to(u.dimensionless_unscaled).value

# this is D times h+, in centimeters
waveform_file = 'GW_strains/s15.0.swbj16.horo.3d.gw.dat'

data = pd.read_csv(waveform_file, sep=' ', names=['time', 'hplus', 'hcross'], skiprows=1)

data['time'] -= min(data['time'])

time = np.linspace(0, max(data['time']), num=5*len(data['time']))

delta_t = time[1] - time[0]

hplus = np.interp(time, data['time'], data['hplus']) / scaling

index_stop = np.searchsorted(time, TIME_STOP)

transition_steps = 100

hplus[index_stop-transition_steps:index_stop] *= (np.arange(transition_steps, 0, step=-1) / transition_steps)**3
hplus[index_stop:] = 0

my_psd = psd_from_string('aLIGOZeroDetHighPower', 2**19, 1, 10)

noise = noise_from_psd(len(time), delta_t, my_psd)

hplus += noise

#%%

f, t, Sxx = signal.spectrogram(hplus, 1/delta_t, nperseg=1<<13)
plt.pcolormesh(
    t, f[:25], Sxx[:25, :], 
    shading='gouraud', 
    norm=mpl.colors.PowerNorm(gamma=.4)
)
# plt.ylim(0, 2e3)

plt.show()

#%%
f, t, Sxx = signal.spectrogram(hplus, 1/delta_t, nperseg=1<<6)
plt.pcolormesh(
    t, f, Sxx, 
    shading='gouraud', 
    norm=mpl.colors.PowerNorm(gamma=.3)
)
# plt.ylim(0, 2e4)

plt.xlim(.498, .502)
plt.show()

#%%

plt.plot((time-TIME_STOP)*1000, hplus)

plt.xlim(-1, 1)
plt.xlabel('Time from end of signal [ms]')
plt.show()


#%%

# timeseries = TimeSeries(
#     data=hplus, 
#     sample_rate=u.Hz / delta_t,
#     t0=t0
# )


# asd = timeseries.asd()

# # asd.plot()

# spectrum = timeseries.q_transform(
#     frange=(200, 10000),
#     # outseg=(t0, time[-1]+t0),
#     qrange=(5, 200), 
#     logf=True,
#     tres=1e-4,
#     # norm=False,
#     whiten=False,
#     fduration=.5,
#     )
# plot = spectrum.plot()
