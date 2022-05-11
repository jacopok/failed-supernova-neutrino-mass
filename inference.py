import numpy as np
from dataclasses import dataclass
import astropy.units as u
import astropy.constants as ac
from tqdm import tqdm

from delays import delay
from flux_estimate import energies, energy_generator

MAX_TIME = .5 # maximum time for the arrival, seconds

@dataclass
class DetectedNeutrino:
    energy: float # MeV
    arrival_time: float # seconds

    def apply_delay(self, neutrino_mass: u.Quantity[u.meV], distance: u.Quantity[u.kpc]):
        self.arrival_time += delay(neutrino_mass, self.energy * u.MeV, distance).to(u.s).value

    def estimated_mass(self, distance: u.Quantity[u.kpc], max_time: float = MAX_TIME):
        delta_t = self.arrival_time - max_time
        if delta_t < 0:
            return 0 * u.meV
        
        return (self.energy * u.MeV * np.sqrt(delta_t * u.s * ac.c / distance)).to(u.meV)


def make_neutrino_list(max_time: float = MAX_TIME):
    
    time = 0
    
    rng = np.random.default_rng()
    
    avg_waiting_time = (1/energy_generator.rate).to(u.s).value
    
    neutrinos = []
    
    while time <= max_time:
        neutrinos.append(
            DetectedNeutrino(
                energy = energy_generator(),
                arrival_time = time
            )
        )
        
        waiting_time = rng.exponential(scale = avg_waiting_time)
        time += waiting_time
    
    return neutrinos

def reconstructed_mass(mass: u.Quantity[u.meV], distance: u.Quantity[u.kpc]):
    max_time = 0.01
    neutrinos = make_neutrino_list(max_time=max_time)
    for n in neutrinos:
        n.apply_delay(mass, distance)

    max_delay_event = max(neutrinos, key=lambda n: n.arrival_time)

    return max_delay_event.estimated_mass(distance, max_time=max_time)



if __name__ == '__main__':

    neutrinos = make_neutrino_list()
    for n in neutrinos:
        n.apply_delay(1*u.eV, 10 * u.kpc)

    plt.scatter(
        [n.arrival_time for n in neutrinos],
        [n.energy for n in neutrinos],
    )
    plt.xlabel('Arrival time [s]')
    plt.ylabel('Energy [MeV]')
    plt.show()
    # plt.savefig('reconstructed_mass.pdf')