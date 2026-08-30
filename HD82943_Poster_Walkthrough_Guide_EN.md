# HD 82943 — Talking Through the Poster

*What to say at each panel and figure, in the order a visitor's eye moves across the poster.*
*Companion to the HD 82943 Conference Talking Points (Q&A) document — use that one for deeper follow-up questions and literature background.*

**How to use this guide:** it follows the poster top-to-bottom, left-to-right. For each panel: a one-line reminder of what's shown, then a short script you can say almost verbatim while pointing at the figure. Keep the full tour under ~5 minutes unless someone wants to go deeper — the Q&A prep document has the deeper material for follow-up questions.

---

## 0. Title, Authors & Abstract

**Opening line**, as someone walks up:

> "This poster is an updated dynamical analysis of HD 82943 — a two-planet system in a 2:1 orbital resonance. We combined new radial-velocity data with an N-body model to pin down the orbits and masses more precisely than before, and we also found a hint of a possible third planet that we're still investigating."

> **Tip:** this single sentence is your "hook" — say it before diving into any panel, so people know the punchline even if they only stay 20 seconds.

## 1. Panel 1 — Orbital Update

**Top-left / top-right of the poster — "Orbital update using literature and archival HARPS and HIRES precise RV data"**

### Figure: RV time series (top-left, big plot)
What's shown: radial velocity [m/s] vs. time [BJD], 2454000–2458000+. Blue stars = HIRES, red circles = HARPS pre-upgrade, green triangles = HARPS post-upgrade. The smooth black curve is the best-fit two-planet model. Below it, the O–C panel shows the residuals (data minus model).

> "This is our full radial-velocity baseline — almost 15 years of data from three instrument/epoch combinations, HIRES in blue and two HARPS eras in red and green. The black curve is our best two-planet fit, and the residuals underneath are flat and small — that's what tells us the two-planet model already explains the data very well."

### Figure: Phase-folded plots (below the time series)
What's shown: two panels, each showing the RV signal folded on one planet's period after removing the other planet's signal — left panel folded on planet b's ~220-day period, right panel on planet c's ~440-day period. Points from all three instruments overlap tightly on a single curve.

> "Here we've folded the data on each planet's own period. You can see all three data sets — HIRES and both HARPS eras — fall right on top of each other on a clean sinusoid. That consistency across independent instruments is a strong check that the periods and amplitudes are right."

### Figure: Corner plot (top-right)
What's shown: the Bayesian posterior distributions from the nested-sampling fit — 2D contours and 1D histograms for P_b, e_b, P_c, e_c, m_b, m_c. Red crosshairs mark the best-fit ("Best lnL") values.

> "This corner plot is the output of our Bayesian fit — it shows not just single best values but the full uncertainty and correlations between parameters. You can see the posteriors are all single, well-defined peaks — no multiple competing solutions — which means the fit is well constrained."

### Table: Parameter values (next to the corner plot)
What's shown: the best-fit orbital parameters at the reference epoch — periods, eccentricities, mutual inclination, and true masses, each with 68.3% confidence intervals.

> "These are our headline numbers: periods of about 220 and 440 days — right at the 2:1 ratio — eccentricities of 0.42 and 0.14, and a mutual inclination near 17 degrees, which pushes the true masses up to about 5.4 and 5 Jupiter masses — roughly three times the minimum masses you'd get without knowing the inclination."

## 2. Panel 2 — N-Body Model & Bayesian Analysis

**Bottom-left of the poster — "N-Body model and Bayesian analysis"**

What's shown: a screenshot of the Exo-Striker software interface — the RV fit and residual panels, plus the fitted-parameter table inside the tool itself. This illustrates the modelling software and workflow, not a new result.

> "This is a look under the hood — we used the Exo-Striker package to run a self-consistent N-body fit, not a simpler Keplerian one, and nested sampling to explore the full parameter space rather than just chasing a single best fit. That's what lets us properly propagate uncertainties into the masses and the resonance analysis."

> **If someone asks "why N-body instead of Keplerian?":** at this level of proximity and eccentricity, the two planets tug on each other enough that their orbits aren't independent ellipses — an N-body model captures that mutual interaction directly, which matters especially for testing resonance and stability.

## 3. Panel 3 — Long-Term Stability & Resonance Analysis

**Bottom-middle of the poster — "Long-term stability and resonance analysis of multiple planet systems"**

### Figure: six time-series panels (t in years, up to 4000 yr)
What's shown, panel by panel: semi-major axis a [au] for planets b and c (blue/red, essentially flat — stable orbits); eccentricity e (oscillating, bounded); period ratio P_c/P_b (tightly oscillating around 2.0); apsidal angle Δω [deg] (magenta, librating); resonant angles θ1 (red) and θ2 (green), both librating around 0°.

> "We integrated the system forward four thousand years to test long-term stability. The semi-major axes stay essentially constant — no drift, no instability. The period ratio stays locked right at 2.0, and both resonant angles oscillate, or librate, around zero degrees instead of circulating all the way around — that libration is the signature of a genuine, stable 2:1 resonance, not just a coincidental period ratio."

### Table: Mean ± semi-amplitude
What's shown: the same quantities (e_b, e_c, P_c/P_b, Δω, θ1, θ2) summarized as a mean value plus the semi-amplitude of their oscillation over the 4000-year integration — not a second, competing fit.

> **Important distinction to make if asked:** this table is time-averaged behaviour over the long integration, while the parameter table in Panel 1 is the point best-fit at the present epoch. They describe different things and are not in tension with each other.

> "Both resonant angles librate with fairly small amplitudes — about 40 degrees or less — around zero, and the apsidal angle does the same. That's an aligned resonant configuration: the two orbits' long axes stay pointed in nearly the same direction over thousands of years."

## 4. Panel 4 — A Likely Third Exoplanet

**Bottom-right of the poster — "A likely third exoplanet in the system"**

What's shown: a periodogram of the residuals from the two-planet N-body fit — dlnL vs. period [days], log scale. A strong, isolated peak is marked with a red arrow near ~1100 days, well above the significance threshold lines.

> "After removing the two-planet signal, we still see a strong, significant peak in the residuals around 1100 days. We list three possible explanations on the poster: a third planet, as suggested before by Baluev and Beaugé in 2014; unmodeled mutual inclination between planets b and c; or stellar activity mimicking a Doppler signal. Right now we think a third planet is the most likely explanation, but we're not calling it confirmed — we still need to rule out stellar activity using activity indicators from the HARPS spectra."

> **Keep this exact balance when you say it:** lead with "most likely explanation," not "confirmed planet." That phrasing matches exactly what's written on the poster and avoids overclaiming.

## 5. Panel 5 — Summary and Conclusions

**Bottom-right corner of the poster — "Summary and conclusions"**

What's shown: the closing text box — no figure, just the take-home statement of the poster.

> "So, to sum up: using the most extended HIRES and HARPS data set assembled for this system so far, we give the most precise characterization of HD 82943 to date — confirming it's a stable, coplanar, significantly inclined 2:1 resonant system with true masses about three times the minimum masses — and we flag a promising but not-yet-confirmed hint of a third planet for follow-up work."

## 6. Suggested Tour Order & Timing

- **~20 sec** — opening hook (Title/Abstract box).
- **~90 sec** — Panel 1: point at the RV time series and the parameter table; skip the corner plot unless they ask about uncertainties.
- **~30 sec** — Panel 2: one sentence on the method, don't dwell on the screenshot.
- **~60 sec** — Panel 3: point at the resonant-angle libration plots — this is the physical proof of the resonance.
- **~60 sec** — Panel 4: the periodogram — this is usually where people get curious and start asking questions.
- **~15 sec** — Panel 5: close with the summary line, then open the floor for questions.

> **If you're short on time:** Title/Abstract → RV time series → resonant-angle plots → periodogram → summary line covers the whole story in under 3 minutes.

---
*Companion to the HD 82943 Conference Talking Points (Q&A) document — use that one for deeper follow-up questions and literature background.*
