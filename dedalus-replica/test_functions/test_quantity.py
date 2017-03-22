"""
Usage for Conserved.py

python3 conserved.py --conserve=<u>

Usage:
    conserved.py [--file=file> --quantity=<quantity> --tolerance=<tolerance>]

Options:
    --quantity=<quantity>        quantity to test
    --file=<file>                file to test
    --tolerance=<tolerance>      tolerance for conservation e.g. 0.01 for 1%

"""

import sys
import h5py
from docopt import docopt

# parse command arguments
args = docopt(__doc__)

# Get command line options
quantity = args['--quantity']
file = args['--file']
tolerance = args['--tolerance'] or 0.01

# Open file with hdf5
h5_file = h5py.File(file, mode='r')

# If we are checking for a conservation
u = h5_file['tasks'][quantity]

# Check if quantity is conserved
# tolerance = 0.05

def tolerant(x1, x2, tol):
    return (x1 * (1. + float(tol)) > x2) != (x1 * (1. - float(tol)) > x2)

def conserve(x):
    if tolerant(x[0], x[-1], tolerance):
        print("Quantity conserved")
    else:
        sys.exit("Quantity not conserved")

conserve(u)                                                                                                                                   
