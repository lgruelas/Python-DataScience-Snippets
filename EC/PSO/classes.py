import numpy as np
import copy as cp

class Particle:
    def __init__(self, d, space):
        self.velocity = np.zeros(d, np.float64)
        self.position = np.array([np.random.uniform(space[i], space[i+1]) for i in xrange(0, d*2, 2)])
        self.best_position = cp.deepcopy(self.position)
        self.best_score = None


class Population:
    def __init__(self, n, d, space):
        self.particles = [Particle(d, space) for __ in xrange(n)]
    def getParticles(self):
        for particle in self.particles:
            yield particle