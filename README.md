# EPIC 211038138.01: a 1.4 Earth-radius planet candidate on a 9.9-day orbit around an M dwarf in the Pleiades field

Advait Paliwal (independent researcher, advaitpaliwal@gmail.com), 2026-10-11.

A dip in brightness of about 0.2% repeats every 9.92 days in K2 Campaign 4 (2015) photometry of EPIC 211038138, a mid-M dwarf 121 pc away in the direction of the Pleiades. Seven transits fall in the campaign. If it is a planet, it is about 1.4 times the size of Earth and receives about three times the sunlight Earth does.

| | |
|---|---|
| Host | EPIC 211038138 = TIC 14255552 = Gaia DR3 65884081064415616 = 2MASS J04010579+2334443, M dwarf (TIC Teff 3281 K, R 0.32 R☉), Gaia DR3 parallax 8.293 ± 0.061 mas, G = 16.10, Kp = 15.36, RUWE 0.98 |
| Period | 9.91618 ± 0.00109 d |
| Mid-transit | 2457100.9794 (+0.0024/−0.0025) BJD_TDB |
| Depth / duration | 2028 (+221/−208) ppm / 1.88 ± 0.10 h (EVEREST light curve) |
| Radius | 1.43 ± 0.13 R⊕ (for R★ = 0.321 R☉) |
| Equilibrium temperature / insolation | 366 ± 20 K / 3.0 (+0.7/−0.6) S⊕ |
| Data | K2 C4 (2015 February–April), 30-minute cadence; 7 transits |
| False-positive probability | 0.008 ± 0.003 (TRICERATOPS with MOLUSC Gaia limits, 10 runs); 0.049 without; NFPP 0 |
| Cluster membership | Catalogues disagree: Pleiades member in ZEIT V (94%), Rebull et al. 2016, Ilin et al. 2021 (0.91) and DANCe (0.82); Pk = 0 in Liu et al. 2025; the parallax places it about 15 pc in front of the 135 pc cluster distance adopted by ZEIT V |

Status: **planet candidate**. Not a TOI, CTOI or K2 candidate in the NASA Exoplanet Archive or ExoFOP as of 2026-10-11. Odd and even transits agree (0.2σ), there is no secondary eclipse (80 ± 151 ppm), and the fitted depths from EVEREST, K2SC and K2SFF agree within 1.6σ. The in-transit difference-image centroid sits 1.1″ (5.0σ) from the out-of-transit centroid; the nearest Gaia source is 36.6″ away. TESS (Sectors 43, 44, 70, 71) cannot detect the transit at T = 14.8 (expected SNR below 1.4 per sector). High-resolution imaging, precise space photometry and a radial velocity for cluster membership are the next observations.

## Contents

- `note/figure1_EPIC211038138.png` — C4 EVEREST photometry folded on the fitted ephemeris, 15-minute bins, exposure-integrated median model with posterior draws, residuals
- `data/lc/folded_lc_everest.csv` — the folded data and model shown in Figure 1; `depths_box.json`, `fresh2_depths.json` — depths per reduction and aperture
- `data/fit/` — posterior summary (`posterior_summary_everest.csv`, 40 walkers × 40,000 steps) and fit outputs for EVEREST (with and without the stellar-density prior), K2SC and K2SFF
- `data/vetting/`, `data/injection/` — odd/even, secondary-eclipse, phase-scan and per-transit checks; injection-recovery and null tests
- `data/pixels/` — difference image, per-pixel PLD fit and depth-versus-aperture results, with the same tests on K2-88 b for reference
- `data/fpp/` — false-positive probability runs (scenario tables, MOLUSC summary)
- `data/tess/`, `data/catalogue/`, `data/search/` — TESS coverage and sensitivity, catalogue queries with their URLs (including the VizieR membership tables), and the search detection
- `code/` — search, light-curve, fit, vetting, pixel, FPP, TESS, catalogue and figure scripts

Data: K2 (NASA, via MAST), EVEREST, K2SFF and K2SC high-level science products, TESS (SPOC and TESScut), ESA Gaia DR3, TIC v8. Software: lightkurve, batman, emcee, transitleastsquares, wotan, TRICERATOPS, MOLUSC, tess-point, astropy, matplotlib. Licences: code MIT; text, figures and data CC BY 4.0.

Scripts are kept exactly as run, with the author's absolute working paths (`~/Scratch/k2-hunt`, `~/Scratch/k2-deep`, `~/Scratch/EPIC211038138-work`); edit those paths to rerun them elsewhere.
