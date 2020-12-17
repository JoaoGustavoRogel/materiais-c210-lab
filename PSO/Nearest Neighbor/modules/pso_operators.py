import random
from modules import pso_utils

CRAZINESS_PROBABILITY = 0.02

def adjust_velocity(population):
    population_adjusted = []

    for p in population:
        closest = pso_utils.find_closest(p, population)
        p.velocity = closest.velocity

        population_adjusted.append(p)

    return population_adjusted


def crazinnes(population, bounds, num_dimensions):
    population_crazy = []

    for p in population:
        if random.uniform(0, 1) < CRAZINESS_PROBABILITY:
            new_velocity = []
            for i in range(num_dimensions):
                new_velocity.append(random.uniform(bounds[i][0], bounds[i][1]))

            p.velocity = new_velocity

        population_crazy.append(p)
    
    return population_crazy


def update_position(population, num_dimensions):
    population_updated = []

    for p in population:
        new_position = []

        for i in range(num_dimensions):
            position = p.position[i] + p.velocity[i]
            new_position.append(position)

        p.position = new_position
        population_updated.append(p)

    return population_updated
