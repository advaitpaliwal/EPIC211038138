"""SPOC 2-min PDCSAP (S70, S71) for TIC 14255552: ephemeris propagation, expected SNR, nominal box depth, constrained search, and a TLS run.
Adapted from ../../scripts/tess.py (same propagation, flattening and constrained-search grid) using the SPOC light curves instead of TESScut."""
import json, numpy as np, warnings; warnings.filterwarnings('ignore')
import lightkurve as lk
from wotan import flatten
D = '/Users/advaitpaliwal/Scratch/k2-deep/211038138'
R = json.load(open(f'{D}/fit/result_everest.json'))
T0, eT0 = R['T0_BKJD'][0], max(R['T0_BKJD'][1:]); P, eP = R['P_d'][0], max(R['P_d'][1:]); T14 = R['T14_h'][0]/24; dep = R['depth_ppm'][0]*1e-6
sr = lk.search_lightcurve('TIC 14255552', mission='TESS', author='SPOC', exptime=120); print(sr)
open(f'{D}/tess/spoc_search.txt', 'w').write(str(sr) + "\n"); open(f'{D}/tess/spoc_search.txt.url', 'w').write("lightkurve.search_lightcurve('TIC 14255552', mission='TESS', author='SPOC', exptime=120) -> MAST\n")
out = dict(T0_BKJD=T0, eT0=eT0, P=P, eP=eP, depth_ppm=dep*1e6, sectors={}); T, F = [], []
for r in sr:
    lc = r.download(download_dir=f'{D}/tess', flux_column='pdcsap_flux', quality_bitmask='default').remove_nans().normalize()
    s = int(lc.meta['SECTOR']); t = lc.time.value; f = lc.flux.value
    fl = flatten(t, f, method='biweight', window_length=0.75); ok = np.isfinite(fl); t, fl = t[ok], fl[ok]
    T.append(t); F.append(fl)
    tb = t + 2167.0; n = np.round((np.median(tb) - T0)/P); Tpred = T0 + n*P; eTpred = np.hypot(eT0, n*eP)
    nin = np.sum(np.abs(((tb - T0 + 0.5*P) % P) - 0.5*P) < 0.5*T14)
    rms30 = np.std(fl)/np.sqrt(15)
    ntr = len([e for e in np.arange(np.ceil((tb.min()-T0)/P), np.floor((tb.max()-T0)/P)+1) if np.any(np.abs(tb - (T0+e*P)) < T14/2)])
    best = []
    for dP in np.linspace(-3*eP, 3*eP, 13):
        for sh in np.arange(-3*eTpred, 3*eTpred, T14/4):
            ph2 = ((tb - (Tpred + sh) + 0.5*(P+dP)) % (P+dP)) - 0.5*(P+dP); ii = np.abs(ph2) < 0.5*T14
            if ii.sum() < 10: continue
            best.append((dP, sh, (np.median(fl) - np.mean(fl[ii]))/(np.std(fl)/np.sqrt(ii.sum()))))
    best = np.array(best)
    out['sectors'][s] = dict(npts=int(len(t)), rms_2min_ppm=float(np.std(fl)*1e6), rms_30min_ppm=float(rms30*1e6), n_epochs_from_K2=int(n), sigma_Tpred_h=float(eTpred*24),
        transits_in_data_nominal=ntr, n_in_nominal=int(nin), expected_snr_per_sector=float(dep/(np.std(fl)/np.sqrt(max(nin, 1)))),
        search_max_snr=float(best[:, 2].max()), search_min_snr=float(best[:, 2].min()), search_trials=int(len(best)))
    print(s, out['sectors'][s], flush=True)
t = np.concatenate(T); fl = np.concatenate(F); np.savez(f'{D}/tess/spoc_s70s71.npz', t=t, f=fl)
nin = np.sum(np.abs(((t + 2167 - T0 + 0.5*P) % P) - 0.5*P) < 0.5*T14)
out['combined_expected_snr'] = float(dep/(np.std(fl)/np.sqrt(max(nin, 1))))
from transitleastsquares import transitleastsquares
b = (t[::5], fl[::5])  # 10-min bins by decimation
ii = np.arange(len(t))//5; tb = np.bincount(ii, t)/np.bincount(ii); fb = np.bincount(ii, fl)/np.bincount(ii)
r = transitleastsquares(tb, fb).power(period_min=1, period_max=20, R_star=0.321, M_star=0.30, R_star_min=0.1, R_star_max=1, M_star_min=0.1, M_star_max=1, oversampling_factor=3, duration_grid_step=1.1, use_threads=1, show_progress_bar=False)
i = np.argmin(np.abs(r.periods - P))
out['tls'] = dict(best_P=float(r.period), SDE=float(r.SDE), power_at_P=float(r.power[i]), P_grid_near=float(r.periods[i]), max_power_within_1pct=float(np.max(r.power[np.abs(r.periods/P - 1) < 0.01])))
print(out['tls'])
json.dump(out, open(f'{D}/tess/tess_spoc.json', 'w'), indent=1)
