import numpy as np
from dataclasses import dataclass
import astropy.units as u
import astropy.constants as ac
from tqdm import tqdm

from delays import delay


MAX_TIME = 0.01 # maximum time for the arrival, seconds
EVENT_RATE = 4e3 # events per second
MIN_ENERGY = 7 # MeV
MAX_ENERGY = 30 # MeV

@dataclass
class DetectedNeutrino:
    energy: float # MeV
    arrival_time: float # seconds

    def apply_delay(self, neutrino_mass: u.Quantity[u.meV], distance: u.Quantity[u.kpc]):
        self.arrival_time += delay(neutrino_mass, self.energy * u.MeV, distance).to(u.s).value

    def estimated_mass(self, distance: u.Quantity[u.kpc]):
        delta_t = self.arrival_time - MAX_TIME
        if delta_t < 0:
            return 0 * u.meV
        
        return (self.energy * u.MeV * np.sqrt(delta_t * u.s * ac.c / distance)).to(u.meV)

def make_neutrino_list(rate: float = EVENT_RATE, max_time: float = MAX_TIME):
    
    time = 0
    
    rng = np.random.default_rng()
    
    neutrinos = []
    
    while time <= max_time:
        neutrinos.append(
            DetectedNeutrino(
                energy = rng.uniform(MIN_ENERGY, MAX_ENERGY),
                arrival_time = time
            )
        )
        
        waiting_time = rng.exponential(scale = 1/rate)
        time += waiting_time
    
    return neutrinos

def reconstructed_mass(mass: u.Quantity[u.meV], distance: u.Quantity[u.kpc]):
    neutrinos = make_neutrino_list()
    for n in neutrinos:
        n.apply_delay(mass, distance)

    max_delay_event = max(neutrinos, key=lambda n: n.arrival_time)

    return max_delay_event.estimated_mass(distance)

if __name__ == '__main__':
    
    import matplotlib.pyplot as plt

    masses = np.linspace(1, 120, num=20) * u.meV
    
    n_trials = 20

    reconstructed_masses = np.repeat(np.copy(masses)[:, None], n_trials, axis=1)
    
    for i, mass in tqdm(enumerate(masses)):
        for j in range(n_trials):
            reconstructed_masses[i, j] = reconstructed_mass(mass, 50 * u.kpc)
    
    for j in range(n_trials):
        plt.scatter(masses, reconstructed_masses[:, j], s=1, c='black')

    plt.xlabel('Original mass [meV]')
    plt.ylabel('Reconstructed mass [meV]')
    
    # plt.scatter(
    #     [n.arrival_time for n in neutrinos],
    #     [n.energy for n in neutrinos],
    # )
    # plt.xlabel('Arrival time [s]')
    # plt.ylabel('Energy [MeV]')
    
    plt.savefig('reconstructed_mass.pdf')