import math
from random import random, randint, randrange, uniform
import numpy as np
import matplotlib.pyplot as plt

Iterations = 0
Particle_size = 20
c1 = 0
c2 = 2
D = 20


# Equations
def rosenbrock(x):
    return 100 * square_itself(((x * x) - x + 1)) + square_itself(x - 1)


# Helper methods & class
def square_itself(x):
    return x * x


class Particle:
    def __init__(self, position, velocity):
        self.position = position
        self.velocity = velocity


def pso():
    return 0


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    pso()
