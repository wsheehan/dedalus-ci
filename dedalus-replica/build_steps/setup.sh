# pull dedalus from bitbucket
cd dedalus/src/dedalus
hg pull
hg up -C

# compile cython with setup.py
export MPI_PATH=/home/dedalus/dedalus
export FFTW_PATH=/home/dedalus/dedalus
python3 setup.py build_ext --inplace