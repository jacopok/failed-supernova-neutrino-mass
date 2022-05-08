import numpy as np
import astropy.units as u
import astropy.constants as ac

def cross_section(E):
    return 1.601e-44 * u.cm**2 * (E / u.MeV)**2

E = 5 * u.MeV
L_nu = 1e52 * u.erg/u.s
time = 10 * u.s
D = 10 * u.kpc
detector_mass = 2 * 187e6 * u.kg  # 2*186kton = HyperK
efficiency = .95

flux = L_nu / (4 * np.pi * D**2) / E
N_p = detector_mass / ac.m_p / 2
sigma = cross_section(E)

N_detected = (flux * N_p * sigma * efficiency).si

print(N_detected)
