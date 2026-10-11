# A Temperate 1.4 Earth-radius Planet Candidate on a 9.9-day Orbit around the Pleiades-field M Dwarf EPIC 211038138

Advait Paliwal
Independent researcher, Sterling Heights, MI 48314, USA
advaitpaliwal@gmail.com

## Abstract

I report a transit-like signal on EPIC 211038138 (2MASS J04010579+2334443), an M dwarf at 120 pc in the direction of the Pleiades, in K2 Campaign 4 photometry. A transit fit gives a period of 9.9162 ± 0.0011 d, a depth of 2028 ± 215 ppm and a duration of 1.88 h, implying a radius of 1.43 ± 0.13 R⊕, an insolation of 3.0 S⊕ and an equilibrium temperature of 366 ± 20 K. The star is not a K2 candidate, TOI or CTOI. Seven transits have consistent depths, odd and even depths agree, and there is no secondary eclipse. No Gaia source lies within 36″. With Gaia companion limits, TRICERATOPS gives FPP = 0.008 ± 0.003 and NFPP = 0. The star's Pleiades membership is disputed. The candidate awaits high-resolution imaging.

## Star and search

EPIC 211038138 has Kp ≈ 16, Teff = 3281 ± 157 K, R★ = 0.321 ± 0.011 R☉ and M★ = 0.301 ± 0.021 M☉ (Stassun et al. 2019). Its Gaia DR3 RUWE is 0.98, with no non-single-star solution, and its parallax is 8.29 mas (Gaia Collaboration et al. 2023). Several studies list it as a Pleiades member (Rebull et al. 2016; Rizzuto et al. 2017; Ilin et al. 2021), but its parallax places it about 14 pc in front of the cluster, and the Gaia DR3 kinematic selection of Liu et al. (2025) assigns it zero membership probability. Rizzuto et al. (2017) searched its K2 light curve as part of ZEIT V and reported no candidate. ExoFOP lists no imaging or spectroscopic follow-up.

I searched EVEREST light curves (Luger et al. 2016, 2018) of about 7,300 cool dwarfs within 138 pc observed by K2 (Howell et al. 2014), selected from Hardegree-Ullman et al. (2020), with wotan (Hippke et al. 2019) and Transit Least Squares (Hippke & Heller 2019) over 0.5–30 d. Each detection had to appear at a consistent depth in EVEREST and K2SFF (Vanderburg & Johnson 2014) and in both halves of the campaign. It also had to pass odd–even, secondary-eclipse, shape and stellar-density tests, and have no Gaia neighbour within 12″ bright enough to produce it. The search recovered known K2 planets at their published periods.

## Transit fit

I fitted the EVEREST light curve (29.4-minute cadence, 2015 February 8 to April 20) with batman (Kreidberg 2015) and emcee (Foreman-Mackey et al. 2013). The model integrates over each exposure, assumes a circular orbit, and uses a TIC stellar-density prior and uninformative quadratic limb darkening (Kipping 2013). It gives P = 9.91618 ± 0.00109 d, T0 = 2457100.9794 ± 0.0024 BJD_TDB, Rp/R★ = 0.0409 ± 0.0026, a/R★ = 40.2 ± 2.0, b = 0.25 (+0.19/−0.17), a depth of 2028 (+221/−208) ppm and T14 = 1.88 ± 0.10 h (Figure 1). This implies Rp = 1.43 ± 0.13 R⊕, a = 0.060 AU, an insolation of 3.0 (+0.7/−0.6) S⊕ and Teq = 366 (+20/−19) K (zero albedo, full redistribution). Fitted without the density prior, the transit gives ρ★ = 8.2 ± 3.4 ρ☉, consistent with the TIC value of 9.1 ρ☉.

## Vetting

The seven EVEREST transit depths are consistent (χ² = 4.2 for 6 degrees of freedom). Model fits to K2SC (Aigrain et al. 2016) and K2SFF give 2312 ± 375 and 2924 (+549/−460) ppm, within 1.6σ of EVEREST given their higher noise. Odd and even depths agree to 0.2σ in EVEREST and 0.7σ in K2SC; K2SFF shows 2.5σ. The depth at phase 0.5 is 80 ± 151 ppm, and no other phase exceeds 2.7σ. Injected transits of the same size were recovered in 39 of 40 trials. With the transits masked, the strongest remaining signal has SDE 6.4, against 22.1 for the candidate.

No other Gaia source lies within 36.6″ (nine pixels); the brightest within 60″ has G = 15.0. The difference-image centroid lies 1.1″ from the out-of-transit centroid, formally 5σ, compared with 1.5σ for the known planet K2-88 b in the same campaign. The summed in-aperture signal-to-noise of the difference image is only 0.7, so this offset is poorly constrained, and no catalogued source lies in its direction. At Kp ≈ 16 the pixel data cannot exclude an unresolved blend.

## False-positive probability

I averaged TRICERATOPS (Giacalone & Dressing 2020; Giacalone et al. 2021), run in its K2 mode, over ten runs of 10⁶ draws each, with companion limits from Gaia astrometry and imaging via MOLUSC (Wood et al. 2021). The result is FPP = 0.0084 ± 0.0027 (range 0.005–0.014) and NFPP = 0. Without companion limits the FPP is 0.049. Most of the remaining FPP comes from a planet orbiting an unresolved bound companion. The star has no high-resolution imaging, and Collier et al. (2026) find that small validated planets in their imaging sample needed contrast curves, so I make no validation claim.

## Summary

EPIC 211038138.01 is a temperate 1.4 R⊕ candidate receiving about three times Earth's insolation. If the star belongs to the Pleiades, the planet would be about 125 Myr old. TESS data from Sectors 43, 44, 70 and 71 are too noisy to test it, and the K2 ephemeris has drifted by several hours. High-resolution imaging and a membership determination are the next steps. Code and data are at https://github.com/advaitpaliwal/EPIC211038138.

## Acknowledgments

This paper includes data collected by the K2 mission, funded by the NASA Science Mission Directorate, and obtained from MAST. It uses data from the ESA mission Gaia, processed by the Gaia DPAC.

## Figure 1

K2 Campaign 4 EVEREST photometry of EPIC 211038138 folded on the fitted ephemeris (grey points), with 15-minute bins (black), the exposure-integrated median model and posterior draws (blue) and residuals (bottom).

## References

Aigrain, S., Parviainen, H., & Pope, B. J. S. 2016, MNRAS, 459, 2408
Collier, M., Giacalone, S., Derfer, B., et al. 2026, AAS Journals, accepted, arXiv:2608.21560
Foreman-Mackey, D., Hogg, D. W., Lang, D., & Goodman, J. 2013, PASP, 125, 306
Gaia Collaboration, Vallenari, A., Brown, A. G. A., et al. 2023, A&A, 674, A1
Giacalone, S., & Dressing, C. D. 2020, triceratops, ascl:2002.004
Giacalone, S., Dressing, C. D., Jensen, E. L. N., et al. 2021, AJ, 161, 24
Hardegree-Ullman, K. K., Zink, J. K., Christiansen, J. L., et al. 2020, ApJS, 247, 28
Hippke, M., David, T. J., Mulders, G. D., & Heller, R. 2019, AJ, 158, 143
Hippke, M., & Heller, R. 2019, A&A, 623, A39
Howell, S. B., Sobeck, C., Haas, M., et al. 2014, PASP, 126, 398
Ilin, E., Schmidt, S. J., Poppenhäger, K., et al. 2021, A&A, 645, A42
Kipping, D. M. 2013, MNRAS, 435, 2152
Kreidberg, L. 2015, PASP, 127, 1161
Liu, R., Shao, Z., & Li, L. 2025, AJ, 169, 116
Luger, R., Agol, E., Kruse, E., et al. 2016, AJ, 152, 100
Luger, R., Kruse, E., Foreman-Mackey, D., Agol, E., & Saunders, N. 2018, AJ, 156, 99
Rebull, L. M., Stauffer, J. R., Bouvier, J., et al. 2016, AJ, 152, 113
Rizzuto, A. C., Mann, A. W., Vanderburg, A., Kraus, A. L., & Covey, K. R. 2017, AJ, 154, 224
Stassun, K. G., Oelkers, R. J., Paegert, M., et al. 2019, AJ, 158, 138
Vanderburg, A., & Johnson, J. A. 2014, PASP, 126, 948
Wood, M. L., Mann, A. W., & Kraus, A. L. 2021, AJ, 161, 85
