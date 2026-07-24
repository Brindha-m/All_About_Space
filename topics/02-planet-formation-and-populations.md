# 02 — Planet Formation and Planet Populations

[← Roman and GBTDS](01-roman-and-gbtds.md) · [Course index](../README.md) · [Next: Microlensing →](03-microlensing-fundamentals.md)

## 1. From clouds to planets

A simplified formation sequence is:

1. a molecular cloud collapses;
2. most mass forms a young star;
3. angular momentum leaves a rotating gas-and-dust disk;
4. solid particles collide, stick, fragment, and drift;
5. planetesimals and embryos grow;
6. planets accrete solids and, for sufficiently massive cores, gas;
7. migration and dynamical interactions rearrange the system;
8. the gas disk disperses, leaving an evolving planetary architecture.

Real systems need not follow a single clean path.

![Simple planet-formation sequence](../assets/key-concepts/planet-formation.svg)

## 2. What is a nebula?

A **nebula** is an interstellar cloud of gas (mostly hydrogen and helium) and dust. The word is Latin for "cloud," and historically it described any fuzzy patch of light in a telescope — even other galaxies, before they were recognized as separate systems.

The main types are:

- **Molecular cloud (dark nebula):** cold, dense gas and dust that blocks background starlight. This is the raw material for star formation — step 1 of the sequence above begins here.
- **Emission nebula (H II region):** gas ionized by hot young stars, glowing with its own light. The Orion Nebula is a nearby example and an active stellar nursery.
- **Reflection nebula:** dust scattering the light of nearby stars, often appearing blue.
- **Planetary nebula:** a shell of gas ejected by a dying Sun-like star. Despite the name, it has nothing to do with planets — early observers named it for its round, planet-like appearance in small telescopes.
- **Supernova remnant:** the expanding debris of an exploded massive star.

Why nebulae matter for this course:

- Stars and their planets form from collapsing molecular clouds; the rotating disk left around a young star (step 3 above) is called the **solar nebula** in the history of our own system.
- Dust in nebulae and the wider interstellar medium causes **extinction** and **reddening** along the line of sight — the central complication of the Galactic-context analysis in [topic 06](06-galactic-context-and-dust.md).
- Planetary nebulae and supernova remnants return chemically enriched gas to the Galaxy. That recycling raises the metallicity of later stellar generations, which feeds directly into the metallicity trends discussed in section 8.

## 3. Core accretion

In the dominant **core-accretion** picture:

- dust grows into larger solids;
- solids concentrate and form planetesimals;
- gravitational growth produces rocky or icy cores;
- a sufficiently massive core can rapidly accrete a gaseous envelope before the disk disappears.

This naturally links giant-planet formation to disk lifetime, solid content, and location.

## 4. The snow line

The **snow line** is the disk radius beyond which volatile compounds can condense into solids. More solid material can make core growth efficient beyond this line. It is not a fixed universal distance: it evolves with stellar luminosity and disk conditions.

Microlensing is especially valuable because its sensitivity often lies near or beyond the snow line, where cold planets are difficult for many other methods.

## 5. Disk instability

In sufficiently massive, cool disks, self-gravity may fragment the disk directly. This **disk-instability** channel is generally discussed for rapid formation of massive objects at wider separations. Whether and where it dominates remains an observational question.

## 6. Migration and architecture

Planets interact gravitationally with disk gas and solids:

- **Type I migration:** lower-mass planets exchange angular momentum with the disk.
- **Type II-like migration:** massive planets that strongly perturb or open a gap evolve with the disk.
- **Resonance:** orbital periods become close to integer ratios.
- **Scattering:** close encounters alter eccentricity, inclination, and separation.
- **Secular evolution:** slow, cumulative gravitational exchange reshapes orbits.
- **Tidal evolution:** close-in systems exchange orbital and rotational energy.

Observed architecture is therefore the outcome of both formation and later evolution.

## 7. What is a planet population?

A population is a probability distribution across properties such as:

- mass and radius;
- period and semi-major axis;
- eccentricity and inclination;
- multiplicity;
- host mass, metallicity, and age;
- Galactic position and kinematics.

We rarely infer each dimension independently. Correlations contain formation information.

## 8. Metallicity and stellar mass

**Metallicity** measures the abundance of elements heavier than helium, commonly represented by \([\mathrm{Fe/H}]\). More metal-rich disks generally provide more solids.

The workshop slide below highlights two physical links:

![Stellar mass and metallicity influence protoplanetary disks and observed populations](../assets/slides/planet-populations-metallicity.png)

- stellar mass correlates with disk mass;
- stellar metallicity traces disk solid content;
- giant-planet occurrence rises strongly with host metallicity;
- the dependence for small planets is weaker and more nuanced.

Selection biases must be ruled out before treating an observed trend as causal.

## 9. Important features in observed populations

- **Hot Jupiters:** gas giants on very short-period orbits.
- **Super-Earths:** planets larger/more massive than Earth but smaller than Neptune; terminology varies.
- **Sub-Neptunes / mini-Neptunes:** intermediate-radius planets, often with volatile envelopes.
- **Radius valley:** deficit between common rocky and envelope-bearing populations.
- **Neptune desert:** scarcity of Neptune-size/mass planets at very short periods.
- **Cold giants:** giant planets at larger separations.
- **Brown-dwarf desert:** relative shortage of brown-dwarf companions at close separations.

These are empirical patterns to explain, not rigid natural categories.

## 10. Mass is not radius

Bulk density is:

$$
\rho_p=\frac{3M_p}{4\pi R_p^3}.
$$

Planets with the same radius can have different masses and compositions. Microlensing primarily constrains mass ratio; transits constrain radius ratio. Combining population-level information from both methods is powerful but requires a mass–radius relation with intrinsic scatter.

## 11. From theory to predictions

A formation theory should predict distributions that can be compared after applying the survey selection function:

$$
\text{formation model}
\rightarrow
\text{planet population}
\rightarrow
\text{survey simulator}
\rightarrow
\text{detected synthetic sample}.
$$

Comparing raw model planets with raw detections is generally invalid.

## 12. Check your understanding

1. Why might metallicity affect giant planets more strongly than small rocky planets?
2. Why is the snow line central to Roman microlensing science?
3. How can migration hide a planet's formation location?
4. Why can two planets with equal radius have different compositions?
5. Why is a planetary nebula unrelated to planets, and which type of nebula do planets actually come from?

