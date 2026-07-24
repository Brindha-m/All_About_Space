# 06 — Galactic Context, the Bulge, and Dust

[← Transits](05-transits.md) · [Course index](../README.md) · [Next: Occurrence rates →](07-occurrence-rates.md)

![Galaxy and dust key concept](../assets/key-concepts/galaxy-dust.svg)

## 1. Milky Way structure

Useful Galactic components include:

- **thin disk:** younger, dynamically colder, gas-rich population;
- **thick disk:** older and dynamically hotter;
- **bulge/bar:** dense central stellar structure;
- **stellar halo:** sparse, old, metal-poor stars;
- **dark-matter halo:** dominant extended gravitating component;
- **interstellar medium:** gas and dust between stars.

![Milky Way anatomy](../assets/slides/milky-way-anatomy.png)

The Sun lies in the disk, while Roman looks inward through the disk toward the bulge.

## 2. Why Galactic context enters exoplanet inference

Microlensing event rates depend on:

- density of source and lens populations;
- distances;
- lens mass function;
- velocity distributions;
- binary and remnant populations.

Transit interpretation depends on:

- which stars are observed;
- stellar radius, mass, metallicity, and age;
- distance and extinction;
- crowding and unresolved companions.

Thus the Galaxy is not merely a backdrop; it is part of the selection and physical model.

## 3. Galactic model ingredients

![Workshop list of Galactic-model ingredients](../assets/slides/galactic-model-ingredients.png)

For each stellar population:

- spatial mass-density distribution;
- kinematics;
- age distribution;
- metallicity distribution;
- initial mass function;
- multiplicity and stellar evolution.

For the overall Galaxy:

- three-dimensional dust map;
- extinction law;
- stellar isochrones;
- initial–final mass relation for remnants.

## 4. Dust extinction and reddening

Dust both dims and changes the color of a star:

\[
F_{\lambda,\rm obs}
=
F_{\lambda,\rm intrinsic}\,10^{-0.4A_\lambda}.
\]

Definitions:

- **extinction \(A_\lambda\):** dimming in a particular band;
- **color excess \(E(B-V)\):** observed minus intrinsic color shift;
- **reddening:** stronger removal of short-wavelength light;
- **extinction law:** wavelength dependence of \(A_\lambda\);
- **differential extinction:** extinction varies across a field or with distance.

Infrared light is less extinguished than optical light:

![Milky Way appearance changes strongly with wavelength](../assets/slides/milky-way-infrared-optical.png)

## 5. Why dust is difficult toward the bulge

- dust is clumpy in angle and distance;
- the extinction law can vary by sightline;
- source and lens may lie behind different dust columns;
- colors are needed for stellar properties;
- faint stars can drop below the detection limit;
- extinction and temperature can be degenerate in spectral-energy-distribution fits.

An incorrect dust model changes both the inferred star and the inferred planet.

## 6. Stellar populations and metallicity

Stars carry information about their formation environment:

- age;
- chemistry;
- spatial position;
- velocity and orbit.

Comparing planet occurrence across disk and bulge populations can test whether planet formation depends on Galactic environment. But location alone is not causal: age, metallicity, stellar mass, and selection effects covary.

## 7. Initial mass function and remnants

The **initial mass function (IMF)** describes the distribution of stellar birth masses. Stellar evolution maps birth mass to:

- surviving main-sequence stars;
- white dwarfs;
- neutron stars;
- black holes.

The **initial–final mass relation** affects dark-lens predictions. Microlensing can detect these remnants gravitationally even when they emit little or no light.

## 8. Kinematics

Relative transverse velocity affects microlensing timescale:

\[
t_E=\frac{\theta_E}{\mu_{\rm rel}}.
\]

A short event may indicate:

- low mass;
- high relative proper motion;
- particular lens/source geometry;
- or a combination.

Population-level mass inference therefore needs realistic velocity distributions.

## 9. Forward-model workflow

1. choose a Galactic density and kinematic model;
2. draw stars and remnants from population distributions;
3. evolve stars and assign spectra;
4. apply distance-dependent extinction;
5. project through the instrument and survey schedule;
6. generate microlensing or transit signals;
7. add crowding, noise, and detection rules;
8. compare synthetic observables with real survey data.

## 10. Check your understanding

1. Why can a short microlensing event not automatically be called a low-mass lens?
2. How can dust bias planet-radius inference?
3. Why should planet occurrence not be compared across Galactic components without matching stellar properties?
4. Which Galactic-model ingredients determine remnant-lens predictions?

