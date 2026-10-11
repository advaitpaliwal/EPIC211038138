#!/bin/sh
# Comparison: K2-88 b (EPIC 210750726, C4, Kp 14.59, P 4.6122 d, T0 BJD 2457066.2194 -> BKJD 3066.2194? no: BKJD = BJD-2454833 = 2233.2194; Crossfield+2016 via NEA k2pandc)
cd /Users/advaitpaliwal/Scratch/k2-deep/211038138/pix/cmp_K2-88
/Users/advaitpaliwal/Scratch/k2-deep/.venv/bin/python -I -c "import lightkurve as lk; r=lk.search_targetpixelfile('EPIC 210750726', mission='K2', campaign=4); print(r); r[0].download(download_dir='.')"
echo "MAST via lightkurve.search_targetpixelfile('EPIC 210750726', mission='K2', campaign=4)" > tpf.url
T=$(ls mastDownload/K2/*/*lpd-targ.fits.gz)
/Users/advaitpaliwal/Scratch/k2-deep/.venv/bin/python -I ../../../scripts/pix.py $T 4.6122 2233.2194 1.04 $(/Users/advaitpaliwal/Scratch/k2-deep/.venv/bin/python -I -c "import lightkurve as lk;t=lk.read('$T');print(t.ra,t.dec)") diff_K2-88
WIN=40 /Users/advaitpaliwal/Scratch/k2-deep/.venv/bin/python -I ../../scripts/apdep_win.py $T 4.6122 2233.2194 1.04 apdepth_w40.json
