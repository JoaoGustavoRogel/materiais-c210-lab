from modules.particle import Particle
from modules.plot_utils import PlotUtils
from modules import pso_operators
from modules import pso_utils


if __name__ == "__main__":
    print("Starting")

    num_iterations = 50
    num_particles = 100
    num_dimensions = 2
    bounds = [(-30, +30), (-30, +30)]

    swarm = []
    for i in range(num_particles):
        swarm.append(Particle(num_dimensions, bounds))

    print("Starting iterations")
    i = 0
    while i < num_iterations:
        swarm = pso_operators.adjust_velocity(swarm)
        swarm = pso_operators.crazinnes(swarm, bounds, num_dimensions)
        swarm = pso_operators.update_position(swarm, num_dimensions)

        for p in swarm:
            PlotUtils.plot_particle(p)
        PlotUtils.plot_iteration(i)

        i += 1

    PlotUtils.save()
    PlotUtils.play()
