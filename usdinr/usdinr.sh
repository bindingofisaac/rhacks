#!/bin/sh

python usdinr.py $1 > usdinr.R
Rscript usdinr.R
