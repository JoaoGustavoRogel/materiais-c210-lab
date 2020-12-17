from .particle import Particle
from .plot_utils import PlotUtils

class PSO:

    def __init__(self, num_dimensions, cost_function, bounds, num_particles, max_iterations):
        gbest_err = -1
        gbest_pos = []

        swarm = []
        for i in range(0, num_particles):
            swarm.append(Particle(num_dimensions, bounds))

        i = 0
        while i < max_iterations:
            print(f"i = {i}\tgbest_pos = {gbest_pos}\tgbest_err = {gbest_err}")

            for j in range(0, num_particles):
                swarm[j].evaluate(cost_function)

                if swarm[j].err < gbest_err  or gbest_err == -1:
                    gbest_pos = list(swarm[j].position)
                    gbest_err = float(swarm[j].err)

            for j in range(0, num_particles):
                swarm[j].update_velocity(gbest_pos)
                swarm[j].update_position(bounds)

                PlotUtils.plot_particle(swarm[j])
            
            PlotUtils.plot_iteration(bounds, i)
            i += 1


        PlotUtils.save()
        PlotUtils.play()
        print(f"i = {i}\tgbest_pos = {gbest_pos}\tgbest_err = {gbest_err}")

