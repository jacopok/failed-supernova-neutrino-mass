# Can a measurement of GWs and neutrinos
# from a galactic supernova be used to determine
# the mass of a neutrino?

import numpy as np 
import astropy.units as u
import astropy.constants as ac
import matplotlib.pyplot as plt # type: ignore
import matplotlib as mpl

def delay(
    neutrino_mass: u.Quantity[u.eV],
    neutrino_energy: u.Quantity[u.eV],
    distance: u.Quantity[u.kpc],
) -> u.Quantity[u.ms]:

    gamma = neutrino_energy / neutrino_mass

    # equivalent to 1 - sqrt(1 - 1/gamma**2) = 1 - v
    c_minus_v = 1 / gamma**2 / (1 + np.sqrt(1 - 1 / gamma**2)) * ac.c

    # equivalent to D / c - D / v, since c_minus_v is so small
    return (distance * c_minus_v / ac.c**2).to(u.ms)

if __name__ == '__main__':
    
    cmap = plt.get_cmap('viridis')
    m_min, m_max = 20, 120
    norm = mpl.colors.Normalize(m_min, m_max)

    # neutrino energy
    Es = np.linspace(5, 30) * u.MeV

    # distance to SN, supposing it's in the vicinity of the galactic center
    D = 10 * u.kpc
    
    masses = np.linspace(m_min, m_max, num=20) * u.meV
    
    for mass in masses:
        
        this_delay = delay(mass, Es, D)
        
        plt.plot(this_delay, Es, c=cmap(norm(mass.value)))

    plt.colorbar(mpl.cm.ScalarMappable(norm, cmap), label='Neutrino mass [meV]')
    plt.title(f'SN distance = {D}')
    # plt.legend(loc='upper right')
    plt.xlabel("Delay [ms]")
    plt.ylabel("Energy [MeV]")
    plt.savefig('delays.png')
    plt.close()
