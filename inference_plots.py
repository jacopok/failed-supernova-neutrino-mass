import matplotlib.pyplot as plt
import numpy as np
import astropy.units as u

from tqdm import tqdm

from inference import reconstructed_mass

masses = np.linspace(1, 120, num=20) * u.meV

n_trials = 100

reconstructed_masses = np.repeat(np.copy(masses)[:, None], n_trials, axis=1)

for i, mass in tqdm(enumerate(masses)):
    for j in range(n_trials):
        reconstructed_masses[i, j] = reconstructed_mass(mass, 50 * u.kpc)

probabilities = np.zeros_like(masses.value)

label = 'Reconstructed mass'
for j in range(n_trials):
    plt.scatter(masses, reconstructed_masses[:, j], s=1, c='black', label=label)
    label=None

for i in range(len(masses)):
    probabilities[i] = sum(reconstructed_masses[i, :] > 1e-3 * u.meV) / n_trials

plt.plot(masses, masses, label='True mass')

plt.xlabel('Original mass [meV]')
plt.ylabel('Reconstructed mass [meV]')
plt.legend()
plt.savefig('reconstructed_masses.png')

plt.close()
plt.plot(masses, probabilities, label='Probability of having a neutrino after the threshold')
plt.xlabel('Original mass [meV]')
plt.legend()
plt.savefig('probability.png')