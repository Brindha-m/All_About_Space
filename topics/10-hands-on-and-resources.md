# 10 — Hands-on Roadmap and References

[← Follow-up and future](09-follow-up-and-future.md) · [Course index](../README.md)

![The scientific learning loop](../assets/key-concepts/hands-on-loop.svg)

## 1. Recommended practical sequence

### Exercise A — Point-lens light curve

1. generate times around \(t_0\);
2. calculate \(u(t)\);
3. calculate \(A[u(t)]\);
4. add source and blended flux;
5. inject Gaussian noise;
6. fit \(t_0,u_0,t_E,F_S,F_B\);
7. inspect covariance and residuals.

Questions:

- Which parameters are correlated?
- What happens if \(F_B\) is fixed incorrectly?
- How does cadence affect \(u_0\) and \(t_0\)?

### Exercise B — Binary-lens anomaly

Use a supported microlensing package to:

1. choose \(q,s,\alpha,\rho\);
2. generate a binary-lens curve;
3. fit a single-lens model;
4. inspect the anomaly in residuals;
5. vary \(q\), cadence, and photometric noise;
6. map where the anomaly remains detectable.

### Exercise C — Transit search

1. simulate a periodic transit;
2. add white and correlated noise;
3. detrend the series;
4. run a BLS search;
5. compare recovered and injected periods;
6. introduce dilution and refit the radius ratio;
7. inject an eclipsing-binary false positive.

### Exercise D — Completeness

1. define a grid in period and radius or \(q,s\);
2. inject many signals;
3. run the unchanged detection pipeline;
4. record recovery;
5. plot completeness;
6. estimate an occurrence rate for a synthetic population;
7. compare with known truth.

### Exercise E — Galactic context

1. select a line of sight;
2. draw stars from disk and bulge populations;
3. assign distance, mass, age, metallicity, and velocity;
4. apply three-dimensional extinction;
5. convert physical properties to observed magnitudes;
6. apply survey cuts;
7. compare intrinsic and observed stellar samples.

## 2. Workshop notebooks

The included [Google Colab guide](../SSW2026_Google_Colab_Instructions.pdf) links to:

### Hands-on Session I

- Microlensing setup notebook
- Single-lens notebook
- Binary-lens notebook
- Group-project notebook and event data

### Hands-on Session II

- Galactic-context overview
- Microlensing or transit context notebook
- Galactic-center event project
- Dark-lens project
- SED-fitting project
- Binary-event project

Use the exact notebook links in the PDF because shared-drive and Colab URLs can change independently of these notes.

## 3. Useful software named in workshop material

- [pyLIMA](https://github.com/ebachelet/pyLIMA)
- [MulensModel](https://github.com/rpoleski/MulensModel)
- [VBMicrolensing](https://github.com/valboz/VBMicrolensing)
- [RTModel](https://github.com/valboz/RTModel)
- [BAGLE Microlensing](https://github.com/MovingUniverseLab/BAGLE_Microlensing)
- [Astropy](https://www.astropy.org/)
- [Lightkurve](https://docs.lightkurve.org/)
- [batman](https://lkreidberg.github.io/batman/)

Check each project's current documentation, license, and citation instructions before research use.

## 4. Core reference gateways

- [Roman mission](https://roman.gsfc.nasa.gov/)
- [Roman Science Support Center at IPAC](https://roman.ipac.caltech.edu/)
- [NASA Exoplanet Archive](https://exoplanetarchive.ipac.caltech.edu/)
- [NASA Exoplanet Science Institute](https://nexsci.caltech.edu/)
- [Sagan Summer Workshop recordings](https://www.youtube.com/@SaganSummerWorkshop)
- [NASA ADS literature search](https://ui.adsabs.harvard.edu/)

## 5. Reading topics

Search ADS for review articles on:

- point and binary gravitational microlensing;
- microlensing optical depth and event rate;
- astrometric microlensing;
- exoplanet transit detection and validation;
- exoplanet occurrence-rate inference;
- protoplanetary disks and planet formation;
- Milky Way bulge structure and extinction;
- Roman microlensing and transit yield forecasts.

Prefer recent reviews for orientation, then read the primary papers for equations and assumptions.

## 6. Reproducibility checklist

- Record software and data versions.
- Keep raw data immutable.
- Separate configuration from code.
- Save random seeds.
- Add tests with known truth.
- Preserve rejected candidates and reason codes.
- Store units with quantities.
- Track coordinate frames and time standards.
- Report priors and parameter bounds.
- Publish selection functions with demographic results.
- Cite data, software, and original workshop presenters.

## 7. Group-project template

1. **Question:** one testable sentence.
2. **Background:** physical reason the answer matters.
3. **Data:** origin, units, quality cuts, and sample definition.
4. **Model:** parameters, likelihood, priors, and assumptions.
5. **Validation:** known truth, injections, or independent comparison.
6. **Result:** effect size and uncertainty.
7. **Limitations:** degeneracies and selection effects.
8. **Next step:** one concrete improvement.

## 8. Final concept map

\[
\boxed{
\text{planet formation}
\rightarrow
\text{planet population}
\rightarrow
\text{Roman observables}
\rightarrow
\text{pipeline catalog}
\rightarrow
\text{selection correction}
\rightarrow
\text{Galactic planet census}
}
\]

If you can explain every arrow—and identify the uncertainty introduced at each one—you have the conceptual foundation needed to work through the workshop notebooks.

