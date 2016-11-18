#!/bin/bash

cd ../code/
THEANO_FLAGS=mode=FAST_RUN,device=gpu,floatX=float32,nvcc.flags=-D_FORCE_INLINES  python2 rbm.py

