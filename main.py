import math
import random
import numpy as np
import matplotlib.pyplot as plt

Iterations = 100
Particle_size = 20
c1 = 0.75  # Cognitive
c2 = 1.4  # Social
D = 20  # Dimensions

g_best = []
Particles = []


# Equations
def rosenbrock(particle):
    x = particle.pbest_pos
    final = 0
    for d in range(D):
        final += (100 * square_itself(((x[d] * x[d]) - x[d] + 1)) + square_itself(x[d] - 1))
    return final


# Helper methods & class
def square_itself(x):
    return x * x


class Particle:
    def __init__(self):
        self.position = []  # Need to change later
        self.velocity = []  # Need to change later
        self.pbest_val = 0
        self.pbest_pos = self.position


def initilise_particle(particle):
    pos = []
    vel = []
    for dimension in range(D):
        pos.append((random.random() * 30))
        vel.append((random.random() * 30))

    particle.position = pos
    particle.velocity = vel
    particle.pbest_pos = pos
    particle.pbest_val = 0


def pso():
    global g_best
    for i in range(Particle_size):
        for dimension in range(D):
            Particles.append(Particle)

    for particle in Particles:
        initilise_particle(particle)
    k = 0
    while k < Iterations:
        for particle in Particles:
            for dimension in range(D):
                if rosenbrock(particle) < particle.pbest_val:
                    particle.pbest_val = rosenbrock(particle)

        Particles.sort(key=lambda value: rosenbrock(value), reverse=True)
        g_best = Particles[0].pbest_pos

        for particle in Particles:
            for dimension in range(D):
                vel = particle.velocity[dimension] + (c1 * random.random()) * (
                        particle.pbest_pos[dimension] - particle.position[dimension]) + (random.random() * c2) * \
                      (g_best[dimension] - particle.position[dimension])

                pos = vel + particle.position[dimension]
                particle.position[dimension] = pos
        k = k + 1
    print(g_best)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    pso()
