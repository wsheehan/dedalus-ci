# Source dedalus
source /home/dedalus/dedalus/bin/activate

# Run simulation
python3 simulations/1d_kdv_burgers/simulation.py

# Test that output file exists
bash test_functions/file_exist.sh analysis/1d_kdv_analysis.h5

# Test Results
python3 test_functions/test_quantity.py --file='analysis/1d_kdv_analysis.h5' --quantity='<u>'