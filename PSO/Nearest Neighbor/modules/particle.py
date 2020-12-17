import random

class Particle:
    def __init__(self, num_dimensions, bounds):
        self.num_dimensions = num_dimensions
        self.position = []
        self.velocity = []

        for i in range(self.num_dimensions):
            self.position.append(random.uniform(bounds[i][0], bounds[i][1]))
            self.velocity.append(random.uniform(bounds[i][0], bounds[i][1]))
