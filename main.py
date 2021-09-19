import math
from random import random, randint, randrange, uniform
import numpy as np
import matplotlib.pyplot as plt

Iterations = 0
Particle_size = 20
c1 = 0
c2 = 2
D = 20

Particles = []


# Equations
def rosenbrock(particle):
    x = particle.pbest_pos
    return 100 * square_itself(((x * x) - x + 1)) + square_itself(x - 1)


# Helper methods & class
def square_itself(x):
    return x * x


class Particle:
    def __init__(self):
        self.position = []  # Need to change later
        self.velocity = []  # Need to change later
        self.pbest_val = float('inf')
        self.pbest_pos = float('inf')


def pso():
    for i in range(Particle_size):
        for dimension in range(D):
            Particles.append(Particle)

    k = 0
    while k < Iterations:
        for particle in Particles:
            if rosenbrock(particle.pbest_pos) > particle.pbest_val:
                particle.pbest_val = rosenbrock(particle.pbest_pos)

        Particles.sort(key=lambda value: rosenbrock(value), reverse=True)
        g_best = Particles[0].pbest_pos

        for particle in Particles:
            for dimension in range(D):
                # Calculate velocity
                r = 1
                # Upadate Position
        k = k + 1
    return 0


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    pso()
