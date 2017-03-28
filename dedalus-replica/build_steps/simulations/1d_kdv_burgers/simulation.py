# Import dedalus and key packages
from dedalus import public as de
import numpy as np
import matplotlib.pyplot as plt

de.logging_setup.rootlogger.setLevel('ERROR')

# Create Basis and Domain
x_basis = de.Chebyshev('x', 1024, interval=(-2, 6), dealias=3/2)
domain = de.Domain([x_basis], np.float64)

# Create Problem
problem = de.IVP(domain, variables=['u', 'ux', 'uxx'])
problem.meta[:]['x']['dirichlet'] = True
problem.parameters['a'] = 2e-4
problem.parameters['b'] = 1e-4
problem.add_equation("dt(u) - a*dx(ux) - b*dx(uxx) = -u*ux")
problem.add_equation("ux - dx(u) = 0")
problem.add_equation("uxx - dx(ux) = 0")
problem.add_bc('left(u) = 0')
problem.add_bc('left(ux) = 0')
problem.add_bc('right(ux) = 0')

# Build solver
solver = problem.build_solver(de.timesteppers.RK443)
solver.stop_sim_time = np.inf
solver.stop_wall_time = np.inf
solver.stop_iteration = 1000

# Reference local grid and state fields
x = domain.grid(0)
u = solver.state['u']
ux = solver.state['ux']
uxx = solver.state['uxx']

# Setup smooth triangle with support in (-1, 1)
n = 20
u['g'] = np.log(1 + np.cosh(n)**2/np.cosh(n*x)**2) / (2*n)
u.differentiate('x', out=ux)
ux.differentiate('x', out=uxx)

# Analysis handler
analysis = solver.evaluator.add_file_handler('analysis', iter=5, max_writes=100)

analysis.add_task("integ(u,'x')", layout='g', name='<u>')
analysis.add_task("integ(u**2,'x')", layout='g', name='<uu>')

analysis.add_system(solver.state, layout='g')

# Simulation
import time

# Main loop
dt = 1e-2
start_time = time.time()
while solver.ok:
    solver.step(dt)
    if solver.iteration % 100 == 0:
        print('Completed iteration {}'.format(solver.iteration))

end_time = time.time()
print('Runtime:', end_time-start_time)

# Merge process files
from dedalus.tools import post
post.merge_process_files("analysis", cleanup=True)

# Merge files into one
import pathlib
set_paths = list(pathlib.Path("analysis").glob("analysis_s*.h5"))
post.merge_sets("analysis/1d_kdv_analysis.h5", set_paths, cleanup=True)
