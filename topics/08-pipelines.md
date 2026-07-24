# 08 — Pipelines and Host-Star Characterization

[← Occurrence rates](07-occurrence-rates.md) · [Course index](../README.md) · [Next: Follow-up and future →](09-follow-up-and-future.md)

![Pipeline key concept](../assets/key-concepts/pipelines.svg)

## 1. What is a pipeline?

A pipeline is a reproducible sequence that transforms raw measurements into scientific products. For Roman time-domain science:

\[
\text{detector reads}
\rightarrow
\text{calibrated images}
\rightarrow
\text{sources}
\rightarrow
\text{light curves}
\rightarrow
\text{events}
\rightarrow
\text{physical parameters}
\rightarrow
\text{populations}.
\]

Each arrow has assumptions and can introduce bias.

![Workshop workflow from Roman images to population studies](../assets/slides/images-to-microlensing-populations.png)

## 2. Pixels to calibrated images

Typical corrections include:

- detector nonlinearity and saturation;
- dark current;
- bias/reference-pixel behavior;
- flat-field response;
- bad and unstable pixels;
- persistence;
- cosmic rays;
- geometric distortion;
- time-dependent sensitivity;
- astrometric and photometric calibration.

Calibration flags must propagate so later analyses can exclude or model affected measurements.

## 3. Images to photometry

Crowded-field approaches include:

- **aperture photometry:** sum pixels in an aperture; simple but blend-prone;
- **PSF fitting:** model overlapping point-spread functions;
- **difference imaging:** subtract a reference image and measure variable flux;
- **scene modeling:** jointly fit stars, backgrounds, motion, and detector response.

Roman fields demand precise knowledge of position-dependent and time-dependent PSFs.

## 4. Light-curve conditioning

Before event searches:

- identify invalid cadences;
- estimate uncertainties;
- remove or model common systematics;
- preserve real astrophysical variability;
- avoid fitting away short anomalies or transits;
- track gaps and changing noise.

Detrending must be tested with injections because a visually clean curve can have suppressed signals.

## 5. Microlensing event search

A conceptual sequence:

1. detect statistically significant brightenings;
2. remove known variables and artifacts;
3. fit point-lens models;
4. search residuals or all events for binary/planetary signatures;
5. explore multimodal parameter space;
6. test higher-order effects and degeneracies;
7. attach physical and population-level constraints.

Binary-lens modeling is computationally expensive near caustics. Fast approximations must be validated where they are used.

![Workshop summary from candidate identification to physical inference](../assets/slides/microlensing-pipeline-summary.png)

### Roman microlensing pipeline product layers

The workshop's Roman Microlensing Science Operations System overview separates products by purpose and delivery cadence. Conceptually, the layers include:

- super-sampled reference images;
- object and source catalogs;
- per-object light-curve catalogs;
- variability catalogs;
- microlensing-event catalogs with model parameters;
- detection-efficiency products based on signal injections.

The detection-efficiency layer is as important as the event list for population science: it records which simulated events the pipeline could recover.

![Workshop overview of planned Roman microlensing pipeline products](../assets/slides/roman-msos-pipeline-products.png)

## 6. Transit search and vetting

A conceptual sequence:

1. detrend variability and instrumental signals;
2. search trial periods, phases, and durations;
3. form TCEs above threshold;
4. run diagnostic tests;
5. classify false alarms and astrophysical false positives;
6. fit transit and stellar models;
7. measure pipeline completeness and reliability.

Diagnostics include:

- odd/even depth comparison;
- secondary-eclipse search;
- centroid motion;
- transit shape and density consistency;
- multi-band depth;
- ephemeris matching;
- pixel-level source localization.

## 7. Computational scale

Searching huge numbers of stars across many period/phase/duration combinations creates billions of statistical trials. Consequences:

- low thresholds generate overwhelming false alarms;
- thresholds that are too strict erase small planets;
- GPU/parallel computing may be needed;
- machine learning can triage but creates a learned selection function;
- reproducible software and versioned models become scientific requirements.

## 8. Host-star characterization

![Host-star size controls inferred planet size](../assets/key-concepts/host-star.svg)

Planet properties inherit stellar properties. Inputs can include:

- broad-band photometry and spectral-energy distributions;
- spectroscopy;
- parallax and proper motion;
- stellar-evolution models/isochrones;
- asteroseismology where available;
- extinction and distance priors;
- high-resolution imaging for companions.

Outputs often include:

- effective temperature \(T_{\rm eff}\);
- surface gravity \(\log g\);
- metallicity \([\mathrm{Fe/H}]\);
- mass, radius, age, distance, and extinction.

SED fitting combines stellar-evolution tracks, atmosphere models, measured parallax, dust laws, and multiple photometric filters. The model predicts brightness in each band and is compared with the observed SED.

![Workshop SED-fitting workflow and software examples](../assets/slides/stellar-sed-fitting-tools.png)

Crowding makes unresolved binaries and chance blends a major systematic. Their combined light can mimic a larger, hotter, or differently aged star and can dilute transits or microlensing events.

![Workshop example of biases from unresolved binaries and blends](../assets/slides/unresolved-binaries-and-blends.png)

## 9. Validation and provenance

Every catalog row should be traceable to:

- input data version;
- calibration software version;
- model and prior choices;
- quality flags;
- diagnostic outputs;
- random seeds for simulations;
- candidate disposition history.

Recommended tests:

- unit and integration tests;
- end-to-end synthetic “known truth” challenges;
- injection/recovery;
- repeatability across detector regions and seasons;
- comparison with independent pipelines;
- posterior predictive checks.

Independent community analyses can complement official products with rapid light curves, difference-image cutouts, alternative PSF fitting, moving-object searches, and reproducibility checks. They must still document calibration and avoid presenting preliminary products as final survey catalogs.

![Workshop ideas for independent pipeline investigation-team analyses](../assets/slides/pit-additional-analyses.png)

## 10. From individual events to unbiased samples

The “best characterized” objects are rarely an unbiased population. Demographic samples need explicit, reproducible inclusion criteria. Follow-up decisions can also create selection bias and must be modeled if followed objects define the sample.

## 11. Check your understanding

1. Why should quality flags propagate beyond image calibration?
2. How can detrending reduce completeness?
3. Why does ML vetting require its own selection calibration?
4. How does a stellar-radius bias propagate to transit planets?

