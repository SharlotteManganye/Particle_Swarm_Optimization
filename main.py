"""
-- *********************************************
-- Author       :	Sharlotte Manganye
-- Create date  :   05 January 2021
-- Description  :   main file
-- File Name    :   main.py
--
"""

from pso import *
from fitness_functions import sphere, rosenbrock, ackley, rastrigin, griewank

x0 = [5,5]
# c1 = 1.429
# c2 = 1.429
# inertia_weight = 0.729
num_particles = 30
iterations = 30
function = rosenbrock
position_bounds = [(-10,10),(-10,10)]
opt = pso(x0, objective_function=function, num_particles=num_particles, position_bounds=position_bounds, iterations=iterations)
print(opt)
# # PSO parameters
# x0 = [5, 5]
# position_bounds = [(-10, 10), (-10, 10)]
#
#
# num_particles = 30
# iterations = 100
#
# pso(x0, sphere, num_particles, position_bounds, iterations, verbose=False)
#
#
#
#
#
#
