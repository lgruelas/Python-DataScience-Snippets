import numpy as np
from classes import Particle, Population

# REMAINS
# CHECK FUNCTIONALITY
# WHAT HAPPENS WHEN A PARTICLE GETS OUT OF LIMITS (REFLECTION)


def optimize(n, d, fitness_function, search_space, max_iter):
    population = Population(n, d, search_space)
    best_particle_position = population.particles[0].position
    best_particle_score = fitness_function(best_particle_position)
    for i in population.getParticles():
        if fitness_function(i.position) < best_particle_score:
            best_particle_position = i.position
            best_particle_score = fitness_function(i.position)
    for __ in xrange(max_iter):
        best_particle_position_sofar = []
        best_particle_score_sofar = float('inf')
        for i in population.getParticles():
            i.velocity = 0.8*i.velocity + np.random.rand()*(i.best_position - i.position)*0.5 + np.random.rand()*(best_particle_position - i.position)*0.5
            i.position += i.velocity
            new_score = fitness_function(i.position)
            if new_score < best_particle_score_sofar:
                best_particle_position_sofar = i.position
                best_particle_score_sofar = fitness_function(i.position)
            if new_score < i.best_score:
                i.best_score = new_score
                i.best_position = i.position
        best_particle_position = best_particle_position_sofar
        best_particle_score = best_particle_score_sofar
    counter = 0
    for i in population.particles:
        if (i.position[0] > 5 or i.position[0] < -5) or (i.position[1] > 5 or i.position[1] < -5):
            counter += 1
    print counter
    return best_particle_score, best_particle_position

def ackley(coords):
    x, y = coords
    return -20*np.exp(-0.2*np.sqrt(0.5*(x*x+y*y))) - np.exp(0.5*(np.cos(2*np.pi*x)+np.cos(2*np.pi*y))) + np.exp(1) + 20

if __name__ == "__main__":
    print optimize(20, 2, ackley, [-5, 5, -5, 5], 10000)