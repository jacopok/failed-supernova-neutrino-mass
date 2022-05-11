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

hyperrefoptions:
- linktoc=all
- linkcolor=blue

---

# Neutrino masses from failed supernovae

Can we measure the mass of neutrinos with a multi-messenger detection of a failed supernova?

The idea is the following: neutrinos being massive gives them a slight delay, which depends on energy: 
$$ \Delta t \approx \frac{D}{c} \frac{m^2}{E^2}
$$
which looks like this:

![Delays from neutrinos ](delays.png)

So, in principle, we could use this effect to measure their mass! 
The effect is tiny, less than a millisecond, while the timescale for emission 
is quite long (on the order of 10 seconds) - how might we hope to detect such a signal then?

There is such a thing as a _failed supernova_: we know they happen (although they are quite rare),
they are supernova events for which, at early times ($\lesssim 1 \text{s}$) a black hole is formed,
which abruptly stops the neutrino and gravitational wave emission.

If this is abrupt enough, and if we have both gravitational wave and neutrino data for this event, 
then we can use the GWs to determine the emission end time, and compare to the last neutrino arrival;
if there is a measurable delay, this gives us a _lower bound on a single* neutrino mass_!

Actually, we're not measuring "a neutrino mass"; we will very likely observe the interaction 
of an electron antineutrino, and therefore measure 
$$ m_e = \sum _{i} U_{i e} m_i
$$
where $m_i$ are the three mass eigenstates, and $U$ is the flavor mixing matrix.

Let's make a list of the potential problems with this approach:

1. neutrino statistics: _is there at least one neutrino arriving later than the end of emission_?
1. GW end time determination uncertainty: _can we determine the end of GW emission within sub-millisecond accuracy_?
1. astrophysical delay systematics: the end of emission may not be as sharp as we would need,
   or there is a difference at the source between the end times of GW and neutrino emission.

## Neutrino statistics

The rate of detected neutrinos per unit energy is given in the form 
$$ R = N_p \sigma \Phi \epsilon 
$$
where $N_p$ is the number of protons, $\sigma$ is the cross-section, $\Phi$ is the flux of neutrinos, $\epsilon$ is the detector efficiency (close to 1). 

For HyperHamiokande, the fiducial mass is about 186kilotons of water per tank (and there are two tanks);
this can be converted into a number of protons with $N_P \approx M / m_p \times (10/18)$.

The flux is taken to have the very simplistic form [@vissaniComparativeAnalysisSN1987A2015]
$$ \Phi = \frac{L_\nu }{4 \pi D^2} \times \frac{E_\nu^2 e^{- E_\nu / T}}{6 T^4},
$$
which has the nice characteristic of allowing us to change the average neutrino energy $\langle E_\nu \rangle = 3 T$.

If $L_\nu$ is in ergs per second, this has units of inverse energy, area and time. 

Now, both $L_\nu$ and $T$ (or $\langle E_\nu \rangle$) evolve over time, but not by orders of magnitude,
so for now I've kept them constant. 

The value $T \approx 4 \text{MeV}$ is a good fit to the SN1987A data, so I've taken that.

The cross-section and number of targets depend on the reaction we are discussing, but 
again for simplicity I've just taken Inverse Beta Decay (which is relevant for HyperK),
therefore the cross-section is [@giuntiFundamentalsNeutrinoPhysics2007]:
$$ \sigma (E_\nu ) \approx 1.6 \times 10^{-44} \text{cm}^2 \left( \frac{E_\nu }{\text{MeV}} \right)^2
$$



## GW end time determination uncertainty

It seems [literature search + question during the ET OSB meeting to Adam Burrows + talk with David Radice] 
that there are no actual simulations of the (QNM) GW emission from failed supernovae. 

Until we have those, I work on a best-case-scenario hypothesis: I take a waveform from one of the 
supernovae they simulated ([here](https://arxiv.org/abs/1812.07703)) and chop it at an arbitrary time;
will I be able to recover the burst end time with sufficient precision?

Sky localization error may be an issue: if there is no optical "counterpart"
(star disappering), the localization error may overcome this accuracy.

Barring that, is the end of the signal even detectable within <1ms? 
it seems like that's quite hard when we have even a low amount of noise. 

However, there may be a workaround! 
If the PNS collapses into a BH, it will have some leftover quadrupole, 
and it will emit QNMs! 

Are they detectable? Don't know! 
It'd be good to make some estimates.

It seems like nobody has GW simulations from failed SNe; write to David Radice! 

## Bibliography