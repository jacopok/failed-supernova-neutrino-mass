# Table 12.1 in Maggiore 2

import numpy as np
import astropy.units as u
import astropy.constants as ac

M = 60 * u.Msun

frequency = (.747343 * ac.c ** 3 / (4 * np.pi * ac.G * M)).si

gamma = (.177925 * ac.c**3 / (2 * ac.G * M)).si

print(frequency)
print(gamma)