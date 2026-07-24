# 01 — Roman and the Galactic Bulge Time Domain Survey

[← Foundations](00-foundations.md) · [Course index](../README.md) · [Next: Planet formation →](02-planet-formation-and-populations.md)

![Roman survey concept](../assets/key-concepts/roman-survey.svg)

## 1. What is Roman?

The **Nancy Grace Roman Space Telescope** is a NASA observatory designed for wide-field infrared imaging and surveys. Its Wide Field Instrument combines:

- space-based image stability;
- Hubble-like angular resolution over a much larger field;
- infrared sensitivity;
- repeated observations suitable for time-domain astronomy.

Roman's major astrophysical themes include dark energy, exoplanets, and wide-area infrared astrophysics. For exoplanets, the crucial point is not only image quality but the number of stars measured repeatedly.

![Roman hardware shown during the workshop](../assets/slides/roman-space-telescope.png)

## 2. What is the GBTDS?

The **Galactic Bulge Time Domain Survey (GBTDS)** repeatedly observes dense star fields toward the Milky Way's central bulge. “Time domain” means that change over time is the scientific observable.

The same images can contain:

- microlensing brightenings;
- planetary transits;
- eclipsing binaries;
- variable stars and stellar rotation;
- astrometric motion;
- transient events;
- Solar System objects moving through the field.

The exact field layout, cadence, filters, and observing seasons are survey-design choices. They affect every yield forecast.

## 3. Why observe the Galactic bulge?

Microlensing needs a chance alignment of observer, lens, and source. A dense line of sight supplies:

- enormous numbers of potential source stars;
- foreground lenses in the disk and bulge;
- relative motions that create transient alignments.

The bulge is observationally difficult because it is crowded and dusty. Roman's angular resolution and infrared imaging reduce—but do not eliminate—those challenges.

## 4. Cadence, baseline, and seasons

- **Cadence:** time between observations. Short cadence helps resolve short planetary anomalies and transit ingress/egress.
- **Baseline:** total time spanned by observations. A longer baseline improves period measurement and proper motion.
- **Season:** a contiguous observing window. Gaps create aliases and can leave long-period transits with ambiguous periods.
- **Exposure time:** controls photons, saturation, and observing efficiency.

Survey design is a trade:

- wider field → more stars, but potentially lower cadence;
- more filters → better colors and host characterization, but fewer measurements per filter;
- longer exposures → higher SNR for faint stars, but saturation and reduced cadence;
- more seasons → stronger long-timescale constraints, but competition with other programs.

## 5. Two detection channels, different parameter spaces

**Microlensing**

- Most sensitive to projected planet–host separation near the lens's Einstein ring.
- Measures planet-to-host mass ratio directly from the light-curve geometry.
- Does not require light from the host.
- Events generally do not repeat.

**Transits**

- Strongly favors short periods and edge-on orbits.
- Measures \(R_p/R_\star\) from transit depth.
- Repetition establishes period.
- Host light is central to interpretation.

Their overlap enables internal cross-checks, while their differences broaden the planetary census.

## 6. Roman's value for demographics

Existing detection methods sample different regions of planet mass, radius, period, separation, host type, and Galactic environment.

![Known planets occupy method-dependent regions of parameter space](../assets/slides/known-exoplanets-parameter-space.png)

Roman matters because it should:

- greatly increase cold-planet microlensing statistics;
- discover low-mass and possibly unbound lenses;
- produce a very large transit candidate sample in a new Galactic environment;
- connect planets to host and Galactic properties;
- use one observatory to probe complementary planet populations.

## 7. Data products you should expect conceptually

Even if final archive details evolve, a mature survey normally needs:

- calibrated images;
- source catalogs and astrometry;
- light curves with uncertainties and quality flags;
- event and candidate tables;
- detector and observing metadata;
- injection/recovery products or enough information to derive selection functions;
- documentation and reproducible examples.

## 8. Key principle

Roman is not simply “a larger planet counter.” Its science comes from combining:

$$
\text{time-series data} + \text{physical models} + \text{selection functions} + \text{Galactic context}.
$$

## 9. Check your understanding

1. Why can one image sequence support both microlensing and transit searches?
2. Why is infrared imaging valuable toward the bulge?
3. Name two ways cadence can alter planet yield.
4. Why must every numerical yield state its survey assumptions?

