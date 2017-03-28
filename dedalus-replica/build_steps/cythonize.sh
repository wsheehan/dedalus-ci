# get dedalus source
source /home/dedalus/dedalus/bin/activate

# compile cython with setup.py
export MPI_PATH=/home/dedalus/dedalus
export FFTW_PATH=/home/dedalus/dedalus

cd /home/dedalus/dedalus/src/dedalus/
python3 setup.py build_ext --inplace