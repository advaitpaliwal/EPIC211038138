#!/bin/zsh
# MOLUSC 2 x 100k (RUWE + Gaia contrast) = 200,000 companions, M = 0.300749 Msun (TIC 14255552 = TRICERATOPS M_s), default age.
# Adapted from ../../212726424/fpp_joint (m100k_s21/s22 pattern); run sequentially (3-process cap on this Mac).
F=/Users/advaitpaliwal/Scratch/k2-deep/211038138/fpp_joint
PYM=/Users/advaitpaliwal/Scratch/planet-hunt/tic240488148-companions/.venv-molusc/bin/python
cd $F
for s in 21 22; do
  SEED=$s $PYM -I -W ignore molusc_run.py -v --ruwe --gaia -a $F/molusc_out/m100k_s$s 04h01m05.7991s -- +23d34m44.268s 100000 0.300749 > molusc_out/m100k_s$s.log 2>&1
done
echo MOLUSC_DONE >> molusc_out/pids
