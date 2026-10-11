#!/bin/sh
# 10 joint runs (exp294, molusc) + 1 reference without molusc (none294_0); at most 3 workers (3-process cap).
D=/Users/advaitpaliwal/Scratch/k2-deep/211038138/fpp_joint
(echo none294 0; seq 0 9 | sed "s/^/exp294 /") | xargs -P 3 -n 2 sh -c 'OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 /Users/advaitpaliwal/Scratch/planet-hunt/hunt4/.venv/bin/python -I -u '"$D"'/scripts/run_joint.py "$1" "$2" > '"$D"'/out/run_$1_$2.log 2>&1' sh
echo ALL_DONE > $D/out/done
