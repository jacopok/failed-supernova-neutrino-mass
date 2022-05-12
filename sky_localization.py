import astropy.units as u
import astropy.constants as ac
import numpy as np

D = ac.R_earth
delta_t = 100 * u.us

ratio = (ac.c * delta_t / D).to(u.dimensionless_unscaled).value

print(f'Aligned case: delta = {(np.arccos(1-ratio) * u.rad).to(u.degree)}')
print(f'Orthogonal case: delta = {(np.arcsin(ratio)*u.rad).to(u.degree)}')