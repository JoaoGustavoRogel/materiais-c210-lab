import random

class Particle:
    def __init__(self, num_dimensions, bounds):
        self.num_dimensions = num_dimensions
        self.position = []
        self.velocity = []
        self.pbest_pos = []
        self.pbest_err = -1
        self.err = -1

        for i in range(0, self.num_dimensions):
            self.position.append(random.uniform(bounds[i][0], bounds[i][1]))
            self.velocity.append(random.uniform(bounds[i][0], bounds[i][1]))

    def evaluate(self, cost_function):
        self.err = cost_function(self.position)

        if self.err < self.pbest_err or self.pbest_err == -1:
            self.pbest_err = self.err
            self.pbest_pos = self.position

    def update_velocity(self, gbest_pos):
        w = 0.5
        c1 = 1
        c2 = 1

        for i in range(0, self.num_dimensions):
            r1 = random.random()
            r2 = random.random()

            vel_cognitive = c1 * r1 * (self.pbest_pos[i] - self.position[i])
            vel_social = c2 * r2 * (gbest_pos[i] - self.position[i])

            self.velocity[i] = w * self.velocity[i] + vel_cognitive + vel_social

    def update_position(self, bounds):
        for i in range(0, self.num_dimensions):
            self.position[i] = self.position[i] + self.velocity[i]

            if self.position[i] < bounds[i][0]:
                self.position[i] = bounds[i][0]

            if self.position[i] > bounds[i][1]:
                self.position[i] = bounds[i][1]
            

    