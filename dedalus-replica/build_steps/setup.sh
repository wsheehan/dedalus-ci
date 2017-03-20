# activate dedalus
source dedalus/bin/activate

# pull dedalus from bitbucket
cd dedalus/src/dedalus
hg pull
hg up -C

# compile cython with setup.py
# python3 setup.py build_ext --inplace