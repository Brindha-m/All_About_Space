# 07 — Occurrence Rates and a Galactic Planet Census

[← Galactic context](06-galactic-context-and-dust.md) · [Course index](../README.md) · [Next: Pipelines →](08-pipelines.md)

![Demographics key concept](../assets/key-concepts/demographics.svg)

## 1. What is occurrence rate?

An **occurrence rate** describes the average number or fraction of planets per star in a specified property region and stellar sample.

These are different questions:

- fraction of stars with at least one planet;
- mean number of planets per star;
- differential rate \(d^2N/(d\log P\,d\log R)\);
- rate per host mass or metallicity;
- rate per dex in mass ratio and projected separation.

Every quoted rate needs:

- planet-property domain;
- stellar sample;
- normalization;
- detection model;
- uncertainty.

## 2. The basic correction

If detected planet \(i\) has detection probability \(p_i\), an intuitive estimator is:

$$
f \sim \frac{1}{N_\star}\sum_i\frac{1}{p_i}.
$$

In practice, geometry, window function, pipeline completeness, reliability, parameter uncertainty, multiplicity, and sample selection make hierarchical or forward-model methods preferable.

## 3. Completeness and reliability

- **Completeness:** fraction of real signals recovered.
- **Reliability:** fraction of reported candidates that are real.
- **Purity:** often used similarly to reliability.
- **False-positive probability:** probability a candidate is a nonplanet astrophysical system.
- **Window function:** probability observations cover the required signal.

For transits:

$$
p_{\rm det}
=
p_{\rm geometric}\,
p_{\rm window}\,
p_{\rm pipeline}\,
p_{\rm vetting}.
$$

For microlensing, sensitivity is commonly estimated over event parameters and planet \(q,s\), then summed over monitored events or modeled through a Galactic event-rate simulation.

## 4. The workflow

![From light curves to occurrence rates](../assets/slides/occurrence-rate-workflow.png)

1. define the target-star/event sample;
2. produce a candidate catalog;
3. characterize candidates and contaminants;
4. measure completeness with signal injections;
5. estimate reliability;
6. define a population model;
7. infer model parameters;
8. perform posterior predictive checks.

## 5. Injection and recovery

Inject synthetic signals into:

- calibrated pixels for the most realistic test;
- extracted light curves for cheaper, targeted tests;
- noise simulations only when those simulations have been validated.

Run the same search and vetting path used on real data. Recovery is measured across the relevant parameter space and stellar properties.

An injection test that bypasses detrending, candidate cuts, or human/ML vetting does not calibrate the complete pipeline.

## 6. Binned estimates

![Example grid-based occurrence-rate approach](../assets/slides/occurrence-rate-grid.png)

Binning is interpretable but creates trade-offs:

- bins too small → few planets and unstable estimates;
- bins too large → hide structure and average changing completeness;
- empty bins → upper limits, not zero occurrence;
- uncertain planet parameters → objects move probabilistically between bins.

## 7. Parametric and hierarchical models

A parametric model might use a broken power law:

$$
\frac{d^2N}{d\log P\,d\log R}
=
C\,g(P)\,h(R).
$$

A hierarchical model marginalizes each object's uncertain true properties rather than fixing point estimates. It can jointly model:

- population parameters;
- candidate reliability;
- stellar-property uncertainty;
- mass–radius relations;
- host-dependent trends.

Model flexibility should be justified by data; an overly rigid model can manufacture smooth structure.

## 8. Microlensing occurrence coordinates

Microlensing naturally measures:

- mass ratio \(q\);
- projected separation \(s\) in Einstein-radius units.

Physical planet mass and AU separation require lens mass and geometry. Demographics can therefore be done:

- directly in \((q,s)\), minimizing conversion assumptions;
- in physical mass/separation, using event-by-event constraints or a Galactic model.

State which space is being inferred.

## 9. Combining transits and microlensing

The two methods do not measure identical variables:

- transit: radius ratio and period;
- microlensing: mass ratio and instantaneous projected separation.

A combined census needs:

- stellar population matching;
- mass–radius relation with intrinsic scatter;
- orbital projection and eccentricity model;
- multiplicity model;
- method-specific selection functions;
- shared definitions and uncertainty propagation.

The reward is broad sensitivity from hot, short-period planets to cold, wide-orbit planets.

## 10. Demographics correction illustrated

![Observed transit planets become occurrence rates after corrections](../assets/slides/transit-demographics-corrections.png)

The observed clumps can shift after correcting for:

- incompleteness;
- reliability;
- transit probability;
- target-star distribution.

## 11. Common mistakes

- treating all candidates as certain planets;
- dividing detections by stars without selection correction;
- mixing unlike stellar samples;
- quoting a yield or rate without its domain;
- ignoring parameter uncertainty near bin boundaries;
- using the same data to tune cuts and claim unbiased completeness;
- comparing methods in radius versus mass without a probabilistic conversion.

## 12. Check your understanding

1. What is the difference between completeness and reliability?
2. Why does an empty bin not imply zero occurrence?
3. Why is \((q,s)\) a natural microlensing demographic space?
4. What assumptions connect a microlensing separation to transit period?

