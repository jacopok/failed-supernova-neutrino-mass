# Neutrino masses from failed supernovae

Can we measure the mass of neutrinos with a multi-messenger detection of a failed supernova?

The idea is the following: neutrinos being massive gives them a slight delay, which depends on energy: 
$$ \Delta t \approx \frac{D}{c} \frac{m^2}{E^2}
$$
which looks like this:

![figure](delays.png)

So, in principle we can use this effect to measure their mass! 
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
1. astrophysical delay systematics: the end of emission is not as sharp as we would need / 
   there is a difference at the source between the end times of GW and neutrino emission.