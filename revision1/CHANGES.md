Changes made in Revision 1 of the research note. The revised note text is with the journal and is not in this repository; the figure, new runs, scripts and source files it cites are in this folder. Paths in this file are the author's working paths.

# AAS82184 R1 (EPIC 211038138): changes from submission8/rnaas8.md

Body 956 words (Star and search to Summary, headings excluded, same count as AAS82088 R1's 887), abstract 139 words.
KD = ~/Scratch/k2-deep/211038138, R = ~/Scratch/planet-hunt/revision-82184.

## Editor question 1 (difference analysis coverage)
- New paragraph opening: "Campaign 4 is the only K2 campaign of this star; TESS Sectors 43, 44, 70 and 71 are too noisy to detect the transit." (KD/tess/tess_spoc.json: expected SNR 0.60/0.69; FACTS line 170.)
- Difference-image method now described (16 in-transit cadences, eight closest-pointing out-of-transit cadences within 1.5 d, 60 random-phase noise images), per ~/Scratch/k2-deep/scripts/pix.py lines 3-4, 18-30.
- Centroid rerun at the fitted ephemeris (old run used the search ephemeris, 22 cadences): offset 1.09″ / 5.0σ -> **1.18″ (0.30 px) / 2.1σ**; centroid error 0.052,0.121 -> 0.143,0.184 px. Source R/out/diff_c04_fitephem.json. Removed the "formally 5σ ... K2-88 b 1.5σ ... summed S/N 0.7" sentences.

## Editor question 2 (χ² definitions)
- Per-transit χ² defined in text (median flux 1.88 h-0.5 d from mid-transit minus mean within ±0.66 h; error = OOT std / √n_in; χ² about the inverse-variance weighted mean). Code ~/Scratch/k2-deep/scripts/vet.py lines 9-23.
- All vetting rerun at the fitted ephemeris (P 9.9161806, T0 BKJD 2267.97937, T14 1.879 h) with R/scripts/vet_fitephem.py (vet.py with output redirected); outputs R/out/vetfit_{everest,k2sc,k2sff}.json. Changes:
  - EVEREST per-transit χ² 4.2/6 -> **2.8/6** (2.808)
  - odd/even EVEREST 0.2σ -> **0.03σ**; K2SC 0.7σ -> **0.6σ**; K2SFF 2.5σ -> **1.0σ**
  - phase 0.5: 80 ± 151 -> **83 ± 165 ppm**; max other phase 2.7σ -> **2.8σ** (2.767)
- New sentence pointing to Figure 1 single transits, S/N 4.3-4.9 (prerev/211038138/make_figs.log).

## Editor question 3 (neighbour removal in TRICERATOPS)
- Stated "No neighbours were removed", with the two Gaia sources in the 40″ field (G 19.5 at 36.6″, 16.2 at 38.6″) given zero probability because of negligible aperture flux (prerev/scripts/trc_neigh.json: flux ratios 3e-23, 1e-23; tdepth 0). n_stars = 3 in all runs (KD/fpp_joint/run_results_exp294.csv).
- Abstract: "With Gaia companion limits and no neighbours removed".
- FPP range given exactly, 0.0045-0.0138 (was 0.005-0.014); FPP 0.0084 ± 0.0027, NFPP 0 unchanged (KD/fpp_joint/summary.json).
- Bound-companion share quantified: STP is 94% of FPP (summary.json scenarios; 0.00791/0.00842).

## Editor question 4 (detrending)
- Search: wotan biweight, **0.4 d window, no transit mask**, clip +3σ/−20σ (~/Scratch/k2-hunt/scripts/k2tls_hunt.py lines 33-38). SDE 22.1 added (KD/inj/real.json).
- Fit: wotan biweight **0.75 d**, transit mask ±0.75 × search duration = about ±1.75 h on the search ephemeris, trend interpolated, OOT clip +4σ/−8σ (~/Scratch/k2-deep/scripts/lcs.py flat()); mask margin ≥ 41 min against the fitted transit (prerev/scripts/chi2_defs.log). 183 points within 7 h (fit.py line 9, reproduced: 183 at duration 2.34 h).

## Editor question 5 (unfolded light curve)
- Figure 1 replaced by the three-panel prerev figure (folded, unfolded C4 with trend, four single transits): final/figure1_combined_EPIC211038138.png, copied unchanged from prerev/211038138/. Caption rewritten.

## Editor question 6 (MOLUSC)
- "imaging via MOLUSC" removed. Now: RUWE and Gaia contrast tests only, no imaging; 200,000 generated, 61.5% kept (123,009; KD/fpp_joint/molusc_summary.txt); kept companions replace TRICERATOPS's bound-companion prior. Without MOLUSC 0.049 (run_results_none294.csv).

## Other PREREV fixes
- Kp ≈ 16 -> **Kp = 15.36 (EPIC)** in Star and search, and Kp = 15.4 in Vetting (FACTS line 26; TPF KEPMAG 15.358).
- No high-resolution imaging stated in the Star section, abstract and FPP section. ExoFOP TIC 14255552 refetched 2026-10-15 (R/_sources/exofop_tic14255552_2026-10-15.json, byte-identical to the 2026-10-11 copy): imaging [], spectroscopy [], only a UKIRT WFCAM K image file.
- Affiliation line: "Independent researcher" only; postal address removed.
- "the planet would be about 125 Myr old" -> "the candidate would be".
- TESS mention moved from Summary to Vetting.

## Unchanged (rechecked against KD/fit/result_everest.json)
P 9.91618 ± 0.00109 d, T0 BKJD 2267.97937 = BJD 2457100.9794, Rp/R★ 0.0409, a/R★ 40.2, b 0.25, depth 2028 (+221/−208), T14 1.88 h, Rp 1.43, S 3.0, Teq 366; no-prior ρ★ 8.2 ± 3.4 (result_everestnorho.json); K2SC 2312, K2SFF 2924 ppm; injection 39/40, null SDE 6.35.

## Files
- final/rnaas_rev1.md, final/Paliwal_EPIC211038138_RNAAS_rev1.docx (built with tools/mkdocx.py, as for AAS82088 R1; figure 6.0 in wide), final/figure1_combined_EPIC211038138.png, final/response.txt (draft reply letter).
