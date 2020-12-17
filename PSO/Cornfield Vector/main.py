from modules.functions import Functions
from modules.particle import Particle
from modules.pso import PSO

if __name__ == "__main__":
    
    num_dimensions = 2
    cost_function = Functions.sphere
    input_bounds = [(-2, +2), (-2, +2)]
    num_particles = 100
    max_iterations = 30

    PSO(num_dimensions, cost_function, input_bounds, num_particles, max_iterations)