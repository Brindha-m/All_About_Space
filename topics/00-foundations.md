# 00 — Astronomy and Statistics Foundations

[← Course index](../README.md) · [Next: Roman and GBTDS →](01-roman-and-gbtds.md)

## 1. The minimum astronomy vocabulary

- **Nebula:** an interstellar cloud of gas and dust. Cold, dense molecular clouds are the birthplaces of stars; glowing emission nebulae surround hot young stars; planetary nebulae are shells ejected by dying Sun-like stars. See [topic 02](02-planet-formation-and-populations.md) for the types and their role in planet formation.
- **Star:** a self-gravitating sphere powered mainly by nuclear fusion.
- **Planet:** a much lower-mass body orbiting a star or stellar remnant. A **free-floating planet** is not bound to a star.
- **Exoplanet:** a planet outside the Solar System.
- **Host star:** the star a detected planet orbits.
- **Orbit:** repeated motion governed primarily by gravity.
- **Orbital period, \(P\):** time required to complete one orbit.
- **Semi-major axis, \(a\):** a measure of orbital size; for a circular orbit it is the radius.
- **Inclination, \(i\):** the orbit's tilt to our line of sight. An edge-on orbit has \(i\approx90^\circ\).
- **Mass, \(M\):** controls gravitational influence.
- **Radius, \(R\):** controls size, transit depth, and—in combination with mass—bulk density.
- **Luminosity:** total power emitted by an object.
- **Flux:** received power per unit area; it falls approximately as \(1/d^2\).
- **Magnitude:** logarithmic brightness scale. A lower magnitude means a brighter source.

![Light becomes fainter with distance](../assets/key-concepts/light-and-distance.svg)

## 2. Essential units

- **AU:** average Earth–Sun distance.
- **pc (parsec):** distance at which 1 AU subtends 1 arcsecond; \(1\,\mathrm{pc}\approx3.26\) light-years.
- **kpc:** 1,000 parsecs, convenient for Galactic distances.
- **arcsecond:** \(1/3600\) degree.
- **milliarcsecond (mas):** \(10^{-3}\) arcseconds.
- Planet quantities are often reported in Earth or Jupiter units: \(M_\oplus, R_\oplus, M_J, R_J\).

## 3. Light, spectra, and detectors

Light is an electromagnetic wave. Wavelength determines the observational band:

- Optical: roughly 400–700 nm.
- Near-infrared: roughly 0.7–5 μm.
- Roman's infrared sensitivity matters because dust blocks optical light toward the Galactic plane more strongly than infrared light.

A telescope records **pixels**, not planets. A simplified chain is:

1. photons arrive at a detector;
2. detector electronics turn charge into pixel values;
3. calibration removes instrumental signatures;
4. photometry estimates a star's brightness;
5. repeated measurements form a **light curve**;
6. models test whether the light curve contains a transit or microlensing event.

## 4. Kepler's third law

For planet mass much smaller than stellar mass:

\[
P^2 \simeq \frac{4\pi^2a^3}{GM_\star}.
\]

For Solar units this becomes approximately:

\[
\left(\frac{P}{1\,\mathrm{yr}}\right)^2
=
\frac{\left(a/1\,\mathrm{AU}\right)^3}{M_\star/M_\odot}.
\]

This connects an observed period to orbital scale when stellar mass is known.

## 5. Probability and inference

Exoplanet surveys never detect every planet. Keep these terms separate:

- **Population:** the real but partly hidden set of planets.
- **Sample:** stars or events included in an analysis.
- **Observable:** what the instrument measures, such as flux versus time.
- **Model parameters:** quantities used to predict data.
- **Likelihood:** probability of the observed data given model parameters.
- **Prior:** information assumed before considering the current data.
- **Posterior:** updated probability distribution after combining prior and likelihood.
- **Uncertainty:** a distribution or interval, not merely a plus/minus decoration.

Bayes' theorem:

\[
p(\theta\mid D)
=
\frac{p(D\mid\theta)\,p(\theta)}{p(D)}.
\]

Here \(\theta\) denotes parameters and \(D\) the data.

## 6. Noise, precision, and accuracy

- **Random noise:** unpredictable scatter; often averages down with more measurements.
- **Systematic error:** a coherent bias from calibration, modeling, or selection.
- **Precision:** repeatability or narrow uncertainty.
- **Accuracy:** closeness to the true value.
- **Signal-to-noise ratio (SNR):** signal amplitude relative to uncertainty.
- **White noise:** uncorrelated measurements.
- **Red noise:** time-correlated noise, dangerous for transit and variability searches.

For independent measurements, SNR often improves roughly as \(\sqrt{N}\). Correlated noise breaks that simple rule.

## 7. Selection effects

A survey preferentially detects some objects:

- large planets make deeper transits;
- short periods produce more repeated transits;
- high-magnification microlensing events can reveal lower mass ratios;
- faint and crowded stars are harder to measure;
- dust changes which stars enter the sample.

Therefore, the detected distribution is:

\[
\text{observed population}
\sim
\text{true population}\times\text{selection function}.
\]

The central goal of demographics is to estimate the true population while accounting for this filter.

## 8. Check your understanding

1. Why can a precise measurement still be inaccurate?
2. If a star is twice as far away, by what factor does its flux change?
3. Why does an exoplanet catalog not directly give an occurrence rate?
4. Which quantity does a transit measure most directly: planet mass or radius ratio?

**Answers:** (1) systematic bias; (2) one quarter; (3) detections are filtered by selection and reliability; (4) radius ratio.

