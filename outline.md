---
# generate pdf with 
# pandoc --citeproc outline.md -o outline.pdf
# (ensure you have pandoc >2.11 installed)
title: Neutrino masses from failed supernovae
author: Jacopo Tissino
bibliography: Neutrinos.bib
abstract: |
  Can we measure neutrino masses using a multimessenger detection of a failed supernova?

link-citations: true
pdf-engine: xelatex

hyperrefoptions:
- linktoc=all
- linkcolor=blue

geometry: "left=3cm,right=3cm,top=2cm,bottom=2cm"
output: pdf_document
---

# Neutrino masses from failed supernovae

## Neutrino masses

We know that (at least two out of three) neutrinos are massive: 
from neutrino oscillations we have two $\Delta m^2$, differences in the squares of their
masses on the order of 
$$ \sqrt{| \Delta m^2 _{\text{atm}}|} \approx 50 \text{meV}
$$
$$ \sqrt{| \Delta m^2 _{\text{sol}}|} \approx 9 \text{meV}
$$

Also, we have bounds from cosmology in the form $\sum _\nu m_\nu < 400 \text{meV}$ roughly,
as well as bounds from neutrinoless double beta decay in the form $m_{ee} \lesssim 100 \text{meV}$ roughly.
I didn't look up the precise numbers, that's the order of magnitude though.

If we measure the propagation of an electron antineutrino, we are looking at
$$ m_{ee} = \sum _{i} U_{i e} m_i
$$
where $m_i$ are the three mass eigenstates, and $U$ is the flavor mixing matrix.

Depending on the mass hierarchy, this mass is likely to be on the order of a few meV, or a few tens of meV.

## Travel delays

Can we measure the mass of neutrinos with a multi-messenger detection of a failed supernova?

The idea is the following: neutrinos being massive gives them a slight delay, which depends on energy: 
$$ \Delta t \approx \frac{1}{2} \frac{D}{c} \frac{m^2}{E^2}
$$
which looks like this:

![Neutrino delays.](delays.pdf)

So, in principle, we could use this effect to measure their mass! 
The effect is tiny, less than a millisecond, while the timescale for emission 
is quite long (on the order of 10 seconds) - how might we hope to detect such a signal then?

There is such a thing as a _failed supernova_: we know they happen (although they are quite rare),
they are supernova events for which, at early times ($\sim 1 \text{s}$) a black hole is formed,
which abruptly stops the neutrino and gravitational wave emission.

If this is abrupt enough, and if we have both gravitational wave and neutrino data for this event, 
then we can use the GWs to determine the emission end time, and compare to the last neutrino arrival;
if there is a measurable delay, this gives us a _lower bound on a single* neutrino mass_!


Let's make a list of the problems with this approach:

1. neutrino statistics: _is there at least one neutrino arriving later than the end of emission_?
1. GW end time determination uncertainty: _can we determine the end of GW emission within sub-millisecond accuracy_?
1. astrophysical delay systematics: the end of emission may not be as sharp as we would need,
   or there is a difference at the source between the end times of GW and neutrino emission.
1. detector uncertainties and background: is the post-end neutrino really astrophysical? what's the uncertainty on the timing?
1. Sky-localization uncertainty and timing.

## Neutrino statistics and setup

The rate of detected neutrinos per unit energy is given in the form 
$$ R = N_p \sigma \Phi \epsilon 
$$
where $N_p$ is the number of protons, $\sigma$ is the cross-section, $\Phi$ is the flux of neutrinos, $\epsilon$ is the detector efficiency (close to 1). 

For HyperHamiokande, the fiducial mass is about 186kilotons of water per tank (and there are two tanks) [@dilodovicoHyperKamiokandeExperiment2017];
this can be converted into a number of protons with $N_P \approx M / m_p \times (10/18) \approx 10^{35}$.

The flux is taken to have the very simplistic form [@vissaniComparativeAnalysisSN1987A2015]
$$ \Phi = \frac{L_\nu }{4 \pi D^2} \times \frac{E_\nu^2 e^{- E_\nu / T}}{6 T^4},
$$
which has the nice characteristic of allowing us to change the average neutrino energy $\langle E_\nu \rangle = 3 T$.

If $L_\nu$ is in ergs per second, this has units of inverse energy, area and time. 
I've taken $L_\nu = 5 \times 10^{51} \text{erg/s}$, and a distance $D = 10 \text{kpc}$.

Now, both $L_\nu$ and $T$ (or $\langle E_\nu \rangle$) evolve over time, but not by orders of magnitude,
so for now I've kept them constant. 

The value $T \approx 4 \text{MeV}$ is a good fit to the SN1987A data, so I've taken that.

The cross-section and number of targets depend on the reaction we are discussing, but 
again for simplicity I've just taken Inverse Beta Decay (which is relevant for HyperK),
therefore the cross-section is [@giuntiFundamentalsNeutrinoPhysics2007]:
$$ \sigma (E_\nu ) \approx 1.6 \times 10^{-44} \text{cm}^2 \left( \frac{E_\nu }{\text{MeV}} \right)^2
$$

For the efficiency I've taken $95 \%$. 

![Reconstructed neutrino masses.](reconstructed_masses.pdf)

![Probability of a post-end neutrino](probability.pdf)

### Neutrino background

I haven't found the expected background rate for HyperK, but if it's on the order of a few Hertz we're good:
the window for this search is very narrow, and it is very unlikely that a background event would be 
detected there. 

If the background is on the order of kHz, we've got bigger problems on our hands.

## GW end time determination uncertainty

It seems [literature search + question during the ET OSB meeting to Adam Burrows + talk with David Radice] 
that there are no actual simulations of the _full_ GW emission from failed supernovae. 

[@panStellarMassBlack2021] do simulate a failed SN, but they:

- compute GWs with the quadrupole formula, so there are no GR effects such as QNMs;
- do not publish their raw waveforms, as far as I can tell;
- stop simulating right at BH formation. 

Also [@cerda-duranGRAVITATIONALWAVESIGNATURES2013] have some older simulations of failed SNe GW emission.
The same three points hold for them.

### Setup

Until we have those, I work on a best-case-scenario hypothesis: I take a waveform from one of the regular, non-failed
supernovae [@radiceCharacterizingGravitationalWave2019] simulated and chop it at an arbitrary time;
will I be able to recover the burst end time with sufficient precision?

The procedure is as follows:

- Take the gravitational waveforms and normalize them to the correct distance;
  - I'm ignoring detector response specifics and approximating $h_+ \approx h_{ij} D_{ij}$
- add in a random realization of noise accoring to the PSD of a given detector;
- whiten the data according to the known PSD
- bandpass the data within some reasonable range.

![Signal with the ET sensitivity.](signal_10.0kpc.pdf)
![Signal with the ET sensitivity.](signal_10.0kpc_zoom.pdf)

### QNMs 

Exponentially decaying oscillations from excited BHs at various multipoles. 
When given a mass, we know the decay rates and the frequencies analytically; 
many of them must be considered for a complete description, but the lowest-frequency one has
$$ f \approx 4 \text{kHz} \left( \frac{M}{3 M_{\odot}}\right)^{-1}
$$

What is the mass of the black hole of interest? It will increase as it accretes over the first milliseconds,
so the frequency of the modes should decrease, and the accretion will probably be noticeably nonisotropic, 
thereby providing a continuous source to the modes for some time. 

This is all speculation, really, but there might be a way to model these signals, since 
they are at least partly analytically known. 
For the purposes of this work, we'd only need to figure out where this emission _starts_ to within some margin.

@easterCanWeMeasure2021 did something vaguely similar, so it's interesting to mention: 
they made an injection study of post-merger waveforms with A+ detectors and ET, 
where the PNS collapses at a certain point, within a 2ms window. 
With A+ sensitivities, they reach uncertainties on the collapse time on the order of 0.3-0.4 milliseconds. 
This is promising! 
The waveforms looked at for failed SNe could be similar. 

### Sky localization error

Sky localization error may be an issue: if there is no optical "counterpart"
(star disappering), the localization error may overcome this accuracy.

A light-millisecond is 300km, distances between detectors are on the order of $10^{4} \text{km}$.

Suppose two detectors are at a distance $D$, and we want to figure out the angular variation $\delta$ 
corresponding to a delay $\Delta t$. 
This will of course depend on the source orientation, but let's look at the limiting cases.

For a source positioned on the connecting line between the two detectors, we will have 
$$ \frac{c \Delta t}{D} \approx \frac{\delta^2}{2}
$$
while for a source positioned orthogonal to the connecting line we will have 
$$ \frac{c \Delta t}{D} \approx \delta 
$$

What do these numbers amount to? Let us consider two detectors separated by Earth's radius, 
which should be rather typical, and a delay $\Delta t = 100 \text{\textmu s}$. Then, 
the value of $\delta$ will range from about a quarter of a degree to five degrees.

So, if we don't precisely know the localization we're screwed!

## Bibliography