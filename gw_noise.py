import numpy as np
from pycbc.psd import from_string as psd_from_string
from pycbc.noise import noise_from_psd
import matplotlib.pyplot as plt

def my_noise_from_psd(psd: np.ndarray, delta_f: float):
    
    rng = np.random.default_rng()
    
    phase = rng.uniform(0, 2*np.pi, size=psd.shape)
    
    asd_with_phase = np.sqrt(psd) * np.exp(1j * phase)
    
    data = np.fft.irfft(asd_with_phase)
    times = np.fft.fftfreq(len(data), delta_f)
    
    return times, data

my_psd = psd_from_string('aLIGOZeroDetHighPower', 2**14, 1, 10)

noise_1 = noise_from_psd(2**14, 2**(-14), my_psd)

time, noise_2 = my_noise_from_psd(my_psd, 1)

plt.plot(noise_1)
plt.plot(noise_2)

plt.show()