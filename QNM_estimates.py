# Table 12.1 in Maggiore 2

import numpy as np
import astropy.units as u
import astropy.constants as ac

M = 3 * u.Msun

frequency = (.747343 * ac.c ** 3 / (4 * np.pi * ac.G * M)).to(u.kHz)

gamma = (1/(.177925 * ac.c**3 / (2 * ac.G * M))).to(u.ms)

print(f'Mass: {M}')
print(f'Lowest QNM frequency: {frequency}')
print(f'Corresponding decay timescale: {gamma}')