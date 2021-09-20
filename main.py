import math
import random
import numpy as np
import matplotlib.pyplot as plt

Iterations = 1000
Particle_size = 20
c1 = 1.496  # Cognitive
c2 = 1.496  # Social
D = 20  # Dimensions
W = 0.7298

g_best = []
Particles = []

fitness_global_initial = float("inf")


# Equations
def rosenbrock(position):
    x = position
    final = 0
    for d in range(D):
        final += (100 * square_itself(((x[d] ** 2) - x[d]))) + square_itself(x[d] - 1)

    return final


# Helper methods & class
def square_itself(x):
    return x * x


def initilise_position():
    pos = []
    for dimension in range(D):
        pos.append((random.randint(-30, 30)))
    return pos


def initilise_velocity():
    vels = []
    for dimension in range(D):
        vels.append(random.uniform(-1, 1))
    return vels


class Particle:
    def __init__(self, position, velocity):
        self.position = position
        self.velocity = velocity
        self.pbest_pos = self.position


def pso():
    global g_best
    global fitness_global_initial
    g_best = initilise_position()

    for i in range(Particle_size):
        for dimension in range(D):
            Particles.append(Particle(initilise_position(), initilise_velocity()))

    k = 0
    while k < Iterations:

        for particle in Particles:
            if rosenbrock(particle.position) < rosenbrock(particle.pbest_pos):
                particle.pbest_pos = np.copy(particle.position)

        Particles.sort(key=lambda value: rosenbrock(value.pbest_pos), reverse=False)
        current_best = np.copy(Particles[0].pbest_pos)

        if rosenbrock(current_best) < rosenbrock(g_best):
            g_best = np.copy(current_best)

        print("Iteration: " + str(k) + "Value: " + str(rosenbrock(g_best)))

        for particle in Particles:
            for d in range(D):
                particle.velocity[d] = (W * particle.velocity[d]) + (c1 * random.random()) * \
                                       (particle.pbest_pos[d] - particle.position[d]) + \
                                       (c2 * random.random()) * (g_best[d] - particle.position[d])

                particle.position[d] = particle.velocity[d] + particle.position[d]

        k = k + 1
    print(g_best)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    pso()
