import numpy as np
import astropy.units as u
import astropy.constants as ac
import matplotlib.pyplot as plt
from astropy.visualization import quantity_support

def cross_section(E):
    return 1.601e-44 * u.cm**2 * (E / u.MeV)**2

def detection_density(
    energies,
    L_nu = 1e52 * u.erg/u.s,
    T = 3 * u.MeV,
    time = 10 * u.s,
    D = 10 * u.kpc,
    detector_mass = 2 * 187e6 * u.kg,  # 2*186kton = HyperK,
    efficiency = .95):
    
    # Vissani 2015, eq. 1
    flux = L_nu / (4 * np.pi * D**2) * energies**2 * np.exp(- energies / T) / 6 / T**4

    N_p = detector_mass / ac.m_p * 10 / 18  # composition of H2O
    sigma = cross_section(energies)

    N_detected = (flux * N_p * sigma * efficiency).to(1 / u.s / u.MeV)
    return N_detected

class VariableGenerator:
    
    def __init__(self, x_pdf, y_pdf, rng=np.random.default_rng()):
        self.x_pdf = x_pdf
        self.y_pdf = y_pdf
        self.rng = rng
        
        self.cumulative = np.cumsum(self.y_pdf * np.gradient(self.x_pdf))
        self.cumulative_prob = (self.cumulative / self.cumulative[-1]).to(u.dimensionless_unscaled).value
        
    def __call__(self, size: tuple[int] = None):
        
        val = self.rng.uniform(0, 1, size=size)
        
        x = np.interp(val, self.cumulative_prob, self.x_pdf.value)
        
        return x

    @property
    def unit(self):
        return self.x_pdf.unit
    
    @property
    def rate(self):
        return self.cumulative[-1].to(u.kHz)

energies = np.linspace(5, 40, num=1000) * u.MeV
energy_generator = VariableGenerator(energies, detection_density(energies))

if __name__ == '__main__':

    print(energy_generator.rate)
    
    values = energy_generator((100000,))
    
    
    with quantity_support():
        plt.plot(energies, detection_density(energies))
        plt.hist(values, bins=100)
    plt.show()
