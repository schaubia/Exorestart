# HD 82943 - Talking Points

*An updated dynamical analysis of the HD 82943 planetary system*
*Conference Q&A prep - main talking points below*

---

## 1. Elevator Pitch

HD 82943 is a Sun-like star (G0, ~1.13–1.15 M☉), known since 2000/2001 for hosting two gas giants locked in a 2:1 orbital resonance (periods of ~220 and ~440 days). The system has been studied repeatedly over the past 20+ years, with conflicting results - different teams have proposed a stable coplanar 2:1 configuration, or alternatives such as a 1:1 resonance or a third planet in a Laplace resonance.

This work presents the most precise dynamical analysis of the system to date, combining extended HIRES/Keck and HARPS RV data (289 points) with a self-consistent N-body model and Bayesian (nested sampling) analysis. The result strongly confirms the classical picture: a stable, coplanar, significantly inclined (~17°) 2:1 resonant system with aligned resonant angles (libration around 0°).

Separately, the residuals show a hint of a possible third planet (period ~1100 days), this is consistent with an earlier hypothesis by Baluev & Beaugé (2014), but not yet confirmed, since stellar activity has not been ruled out as the origin of the signal.

## 2. Historical Framework

* What's new here? - the timeline:*

- **2000-2001 (ESO/CORALIE - Mayor, Udry, Naef et al.):** the two planets are announced sequentially - the longer-period one first, then the shorter-period one.
- **2004 - Mayor et al.:** official publication of the CORALIE orbital solutions.
- **2006 - Lee et al.:** combine CORALIE + new Keck data; show the only stable solutions correspond to the 2:1 MMR, periods ~220 and ~440 days - the classic result cited on the poster.
- **2006 - Goździewski & Konacki:** propose an alternative, less coplanar 1:1 resonant solution (later found to be less well supported).
- **2008 - Beaugé et al.:** propose a third planet in a Laplace resonance (4:2:1), based mainly on CORALIE data.
- **2013 - Tan et al.:** significantly expanded Keck data set; confirm a stable two-planet configuration with aligned apsidal corotation; note a weak, statistically insufficient hint near ~1000 days.
- **2014 - Baluev & Beaugé:** joint CORALIE + Keck analysis; argue for a real additional ~1075-day signal, potentially a third planet, while acknowledging the uncertainty.

> **Takeaway:** the question "is there a third planet?" has been open in the literature for over 15 years - this analysis is the latest, most precise step in that discussion, not the first time it has been raised.

## 3. What the Analysis Shows

**Data & method**
- **Data:** 289 nightly-binned RV points - 167 from HIRES/Keck (weighted rms 4.84 m/s) + 122 from HARPS (pre-/post-upgrade split: rms 2.77 and 3.22 m/s).
- **Method:** self-consistent N-body RV model (Exo-Striker, Trifonov 2019) + nested sampling for Bayesian posterior exploration; coplanar models at different line-of-sight inclinations compared against mutually inclined configurations.

**Orbital result - best fit ("Best lnL", 68.3% percentile errors)**

| Parameter | Value |
|---|---|
| P_b / P_c | 219.82 (+0.16/−0.16) d / 440.44 (+0.62/−0.62) d (ratio ≈ 2.00 - textbook 2:1) |
| e_b / e_c | 0.4209 ± 0.0065 / 0.138 ± 0.014 |
| Mutual inclination i_{b,c} | 17.2 (+1.6/−1.3)° |
| True masses m_b / m_c | 5.40 (+0.44/−0.47) / 5.05 (+0.40/−0.42) M_Jup - ~3.4× the *m* sin *i* values |

**Resonant state**
Both eccentricity-type resonant angles librate around 0° with relatively small amplitude → an aligned 2:1 resonant configuration; the apsidal angle Δω also librates around 0° → apsidal alignment. A long-term (4000-year) N-body integration confirms the stability.

**Reading the poster's two tables correctly**
> **Note:** the second table ("Long-term stability…", column "Mean ± semi-ampl.") is not an alternative fit - it shows the mean and semi-amplitude of oscillation of the same quantities over the long-term integration (how the system "wobbles" over time). The first table (next to the corner plot) is the point best-fit at the reference epoch. The two don't contradict - they answer different questions.

## 4. The Third-Planet Question

** Framing:**

> "Our main, statistically most robust result is a two-planet, coplanar 2:1 resonant system - that is the conclusion we are most confident in. However, in the residuals of the two-planet model we see a statistically significant additional signal with a period of about 1100 days. This is consistent with the hypothesis of a third planet proposed by Baluev & Beaugé (2014), but we are not yet claiming it is confirmed as a real planet - we cannot rule out that the signal originates from stellar activity rather than a planetary Doppler signal. We are therefore currently investigating it further using stellar-activity indicators (S-index, Hα, NaD, CRX, differential line width) from the HARPS spectra."

> **Why not just announce it as a planet?:** a signal in the residuals ≠ a confirmed planet - stellar activity (magnetic cycles, spots, plages) must first be ruled out, since it can mimic a periodic Doppler signal, especially at periods on the order of a thousand days.

## 5. Q&A

**Q: Why do your results differ from previous studies?**
A: They don't differ conceptually - we confirm the classical 2:1 resonant picture (Lee et al. 2006, Tan et al. 2013). The difference is precision: more data (HIRES + both HARPS subsets), a longer baseline, a self-consistent N-body model instead of a Keplerian one, and a full Bayesian uncertainty analysis instead of a single best-fit point.

**Q: How confident are you in the 17° inclination?**
A: It comes from comparing coplanar models at different line-of-sight inclinations within the Bayesian framework - statistically preferred over the edge-on (90°) solution, but with its own uncertainty (+1.6/−1.3°). We quote a confidence interval, not an exact value.

**Q: Could the third-planet signal just be an observational artifact?**
A: Possible - that's why the poster explicitly lists three hypotheses: (1) a third planet, (2) unmodeled mutual inclinations between planets b and c, (3) stellar activity. We are actively testing (3) using spectral activity indicators.

**Q: What's next for this research?**
A: Completing the stellar-activity analysis (comparing S-index/CRX/dLW residuals against the RV residuals) to separate a genuine planetary signal from activity; if confirmed, a full three-planet dynamical model with a stability check.

## 6. The Host Star, Briefly

A G0-type star, slightly more massive and luminous than the Sun: M* ≈ 1.13–1.15 M☉, R* ≈ 1.17–1.2 R☉, T_eff ≈ 5950–6000 K, slightly super-solar metallicity ([Fe/H] ≈ +0.2). Distance ~27 pc (parallax ≈ 36.1 mas).

---

# Appendices
*Reference material - not needed for the talk itself.*

## Appendix A. Literature Notes

**Goździewski & Maciejewski (2001), ApJ 563, L81**
The first paper to raise the question of the system's dynamical stability. Shows that the originally announced two-planet Keplerian solution is self-destructing (unstable), and uses the MEGNO indicator to find the stability zones in parameter space - heuristically identifying a stable initial condition that reproduces the observed RV curve well. First work to identify the 2:1 commensurability as key to stability.

**Lee et al. (2006), ApJ 641, 1178**
Combine the CORALIE data (digitized from the graphs in Mayor et al. 2004) with 23 new Keck measurements. Systematically explore a grid of fits as a function of the outer planet's eccentricity and argument of periastron. The best fit is dynamically unstable, but the minimum is shallow - a wide range of stable solutions exists outside it, all within the 2:1 MMR. They derive periods of ~220 and ~440 days - the value cited on the poster. Conclusion: the system is "almost certainly" in the 2:1 MMR.

**Baluev & Beaugé (2014), MNRAS 439, 673**
*(the file "2013_Baluev_stt2486" is the same paper - stt2486 is its MNRAS DOI suffix; identical to "2014_Baluev1410.1325", already reviewed.)* Purge a systematic annual variation in the CORALIE data and find a clear additional signal with a period of ~1075–1100 days in the residuals, present in all three independent RV subsets. They propose a stable configuration close to a 1:2:5 three-planet resonance - while explicitly noting uncertainty: the third planet "may lie in or slightly outside" the 5:2 resonance, with a mass of only ~0.3 M_Jup.

**Trifonov et al. (2021), AJ 162, 283**
*(the reference used for the activity-indicator table.)* Not specific to HD 82943, but describes the SERVAL pipeline methodology for extracting stellar-activity indicators from HARPS spectra: the chromatic RV index (CRX), differential line width (dLW), and the Hα, Na I D, and Na II D emission lines - exactly the columns present in the provided data files. The reference is correctly chosen for the methodology cited in the stellar-activity section.

**Extra historical trivia:**
- The planets were announced sequentially in 2000 (the longer-period one, b) and 2001 (the shorter-period one, c) by the Geneva team (ESO announcements).
- HD 82943 is notable for an unusually high lithium-6 abundance for its age - one argument for the hypothesis that the star swallowed planetary material in the past.
- A debris disk was discovered around the star (2003, infrared excess) - independent evidence for planetesimal material in the system.
