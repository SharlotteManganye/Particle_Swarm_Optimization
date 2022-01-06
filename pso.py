"""
-- *********************************************
-- Author       :	Sharlotte Manganye  https://github.com/FawazQutami/Particle-Swarm-Optimization-PSO/blob/master/plotting.py
-- Create date  :   05 January 2021
-- Description  :   Cost Functions
-- File Name    :   pso.py
--
"""
# import libraries
from random import random
from random import uniform
import matplotlib.pyplot as plt

class Particle:
    '''
    x0: Intialposition of the particle specified by the user
    bound: Axis bound for each dimension
    ################ EXAMPLE #####################
    If
    X = [x, y, z], dimension = 3 and if
    bound = [(-5, 5), (-1, 1), (0, 5)]
    Then, x∈(-5, 5);
    y∈(-1, 1);
    z∈(0, 5)
    '''

    def __init__(self, x0):   # x0 is the starting position
        self.position = []   #  particle position
        self.velocity = []   #  particle position
        self.personal_best_position = []  #  particle's best position
        self.particle_best_error = -1   #  particle's best error
        self.particle_error = -1  #  particle's error

        for i in range(0, num_dimensions):
            self.velocity.append(uniform(-1, 1))
            self.position.append(x0[i])

# particle evaluation and  check to see if the current position is an individual best
    def evaluate(self, objective_function):
        self.particle_error = objective_function(self.position)
        if self.particle_error < self.particle_best_error or self.particle_best_error == -1:
            self.personal_best_position = self.position
            self.particle_best_error = self.particle_error

# update new particle velocity
    def update_velocity(self, group_best_position):
        c1 = 1.429
        c2 = 1.429
        inertia_weight = 0.729
        for i in range(0, num_dimensions):
            r1 = random()
            r2 = random()
            cognitive_velocity = c1 * r1 * (self.personal_best_position[i] - self.position[i])
            social_velocity = c2 * r2 * (group_best_position[i] - self.position[i])
            self.velocity[i] = inertia_weight * self.velocity[i] + cognitive_velocity + social_velocity

# update the particle's position using the velocity updates

    def update_position(self, position_bounds):
        for i in range(0, num_dimensions):
            self.position[i] = self.position[i] + self.velocity[i]

            # adjust maximum position if necessary
            if self.position[i] > position_bounds[i][1]:
                self.position[i] = position_bounds[i][1]

            # adjust minimum position if necessary
            if self.position[i] < position_bounds[i][0]:
                self.position[i] = position_bounds[i][0]


def pso(x0, objective_function, num_particles, position_bounds, iterations):
    global num_dimensions
    num_dimensions = len(x0)
    group_best_error = -1  # group's best error
    group_best_position = []  # group's best position


# create a swarm

    swarm = []
    for i in range(0, num_particles):
        swarm.append(Particle(x0))

# optimization loop until the stopping criteria is met
    # the algorithm will stop if the maximum iterations is reached
    i = 0
    cost, time = [], []
    while i < iterations:

        for j in range(0, num_particles):
            swarm[j].evaluate(objective_function)

            # determine if current particle is the best (globally)
            if swarm[j].particle_error < group_best_error or group_best_error == -1:
                group_best_position = list(swarm[j].position)
                group_best_error = float(swarm[j].particle_error)

        # cycle through swarm and update velocities and position
        for j in range(0, num_particles):
            swarm[j].update_velocity(group_best_position)
            swarm[j].update_position(position_bounds)
        time.append(i)
        cost.append(objective_function(group_best_position))
        i += 1

    # print('Final output:')
    # print(group_best_position)
    # print(group_best_error)

    print('\nParticle Swarm Optimisation\n')
    print('PARAMETERS\n', '-' * 80)
    print('Population size : ', num_particles)
    print('Dimensions      : ', num_dimensions)
    print('Inertia weight : ', 0.729)
    print('c1              : ', 1.429)
    print('c2              : ', 1.429)
    print('function        : ', objective_function)
    print('RESULTS\n', '-' * 80)
    print('group best error   : ', group_best_error)
    print('group best position    : ', group_best_position)
    print('iterations      : ', i + 1)

# plot global fitness (or cost/objective ) value vs iterations

    plt.plot(time, cost)
    plt.title('Fitness Value vs Iteration')
    plt.xlabel('Iteration')
    plt.ylabel('Fitness Value')
    plt.show()

