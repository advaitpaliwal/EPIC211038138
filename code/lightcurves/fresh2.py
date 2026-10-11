"""Fresh TPF photometry variants for EPIC 211038138 (adapted from ../../scripts/lcs.py fresh()): threshold-3 aperture and pipeline aperture,
corrected with lightkurve SFFCorrector (windows 10/20/40) and PLDCorrector; transits masked; box depth at fixed ephemeris."""
import sys, json, numpy as np, warnings; warnings.filterwarnings('ignore')
import lightkurve as lk
sys.path.insert(0, '/Users/advaitpaliwal/Scratch/k2-deep/scripts'); import lcs
P, T0, T14 = 9.916949, 2238.2271, 2.34/24
D = '/Users/advaitpaliwal/Scratch/k2-deep/211038138'
tp = lk.read(f'{D}/lc/mastDownload/K2/ktwo211038138-c04_lc/ktwo211038138-c04_lpd-targ.fits.gz', quality_bitmask='default')
aps = {'thresh3': tp.create_threshold_mask(3, reference_pixel='center'), 'pipeline': tp.pipeline_mask}
res = {}; best = None
for an, ap in aps.items():
    lc = tp.to_lightcurve(aperture_mask=ap).remove_nans(); lc = lc[np.isfinite(lc.centroid_col.value) & np.isfinite(lc.centroid_row.value)]
    t = lc.time.value; intr = np.abs(lcs.phase(t, P, T0)) < 0.75*T14
    for cn in ['sff10', 'sff20', 'sff40', 'pld']:
        try:
            if cn == 'pld':
                tpm = tp[np.isin(tp.time.value, t)]
                c = lk.PLDCorrector(tpm, aperture_mask=ap).correct(cadence_mask=~np.abs(lcs.phase(tpm.time.value, P, T0)) .__lt__(0.75*T14), pld_order=2, restore_trend=True)
                tt0 = c.time.value
            else:
                c = lk.SFFCorrector(lc).correct(windows=int(cn[3:]), bins=15, cadence_mask=~intr, restore_trend=True); tt0 = t
            f = c.flux.value; m = np.isfinite(f); tt, ff = lcs.flat(tt0[m], f[m]/np.nanmedian(f[m]), P, T0, T14)
            d, e, n = lcs.boxdepth(tt, ff, P, T0, T14)
            res[f'{an}_{cn}'] = dict(npix=int(ap.sum()), depth_ppm=float(d*1e6), err_ppm=float(e*1e6), rms_ppm=float(np.std(ff)*1e6), n_in=n)
            print(an, cn, res[f'{an}_{cn}'], flush=True)
            if best is None or np.std(ff) < best[0]: best = (np.std(ff), f'{an}_{cn}', tt0[m], f[m]/np.nanmedian(f[m]), tt, ff)
        except Exception as ex: res[f'{an}_{cn}'] = repr(ex); print(an, cn, ex)
res['lowest_rms'] = best[1]
np.savez(f'{D}/lc/fresh2.npz', t_raw=best[2], f_raw=best[3], t=best[4], f=best[5])
json.dump(res, open(f'{D}/lc/fresh2_depths.json', 'w'), indent=1)
