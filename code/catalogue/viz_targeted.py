# Targeted VizieR cone (30 arcsec) on K2 candidate / validation / EB / ML-vetting catalogues; adapted from ../../212726424/scripts/viz_targeted.py pattern.
import json, warnings; warnings.filterwarnings('ignore')
from astroquery.vizier import Vizier
import astropy.units as u; from astropy.coordinates import SkyCoord
c = SkyCoord(60.27416*u.deg, 23.57896*u.deg)
found = {}
for kw in ['ExoMiner', 'Valizadegan', 'K2 planet candidates', 'K2 eclipsing binaries', 'K2 candidates', 'K2 false positive', 'K2 transit', 'K2 validated planets', 'young cluster planets K2', 'Pleiades K2']:
    try:
        for k, v in Vizier.find_catalogs(kw).items(): found[k] = str(v.description)[:110]
    except Exception as e: print('find', kw, e)
fixed = ['J/ApJS/244/11','J/AJ/155/136','J/ApJS/222/14','J/AJ/155/21','J/ApJS/226/7','J/AJ/154/207','J/A+A/594/A100','J/MNRAS/461/3399','J/AJ/159/154','J/AJ/161/82','J/AJ/163/244','J/A+A/579/A19','J/PASP/127/1063','J/AJ/151/68','J/AJ/152/47','J/AJ/158/161','J/AJ/160/108','J/AJ/165/68','J/AJ/167/240','J/AJ/154/224']
cats = sorted(set([k for k in list(found) if k] + fixed))
out = {}
v = Vizier(row_limit=50, columns=['**', '_r'])
for k in cats:
    try:
        r = v.query_region(c, radius=30*u.arcsec, catalog=k)
        out[k] = dict(desc=found.get(k, ''), tables={t.meta.get('name', str(i)): [dict((cc, str(row[cc])) for cc in t.colnames[:14]) for row in t] for i, t in enumerate(r)})
    except Exception as e: out[k] = dict(desc=found.get(k, ''), error=str(e))
    print(k, found.get(k, '')[:60], '->', {n: len(x) for n, x in out[k].get('tables', {}).items()} if 'tables' in out[k] else out[k]['error'][:60], flush=True)
json.dump(out, open('vizier_targeted_30as.json', 'w'), indent=1)
