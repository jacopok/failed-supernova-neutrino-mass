import matplotlib.pyplot as plt
import numpy as np
import astropy.units as u

from tqdm import tqdm

from inference import reconstructed_mass

masses = np.linspace(1, 120, num=20) * u.meV

n_trials = 20

reconstructed_masses = np.repeat(np.copy(masses)[:, None], n_trials, axis=1)

for i, mass in tqdm(enumerate(masses)):
    for j in range(n_trials):
        reconstructed_masses[i, j] = reconstructed_mass(mass, 50 * u.kpc)

for j in range(n_trials):
    plt.scatter(masses, reconstructed_masses[:, j], s=1, c='black')

plt.plot(masses, masses)

plt.xlabel('Original mass [meV]')
plt.ylabel('Reconstructed mass [meV]')
plt.show()

