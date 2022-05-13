# Neutrino masses from failed supernovae

Can we measure the mass of neutrinos with a multi-messenger detection of a failed supernova?

Neutrinos being massive gives them a slight delay, 
which looks like this:

![figure](delays.png)

In this repo, one can find estimates and mock data towards this purpose.
The file `overview.md` provides an overview.

## Scripts

### Neutrinos

- `flux_estimate.py`: define a neutrino energy distribution, generate energies stochastically
- `inference.py`: generate neutrinos in time and energy, delay them in time
- `inference_plots.py`: plot the probabilities and reconstructed masses
- `delays.py`: plot the delays as a function of energy and mass

### Gravitational waves

- `gw_mock.py`: add signal to simulated noise, whiten, bandpass, plot
- `QNM_estimates.py`: very simple frequency estimates for BH QNM
- `gw_sounds.py`: save the SN waveforms as audio files
- `gw_noise.py`: unused, experiment in generating noise manually