from matplotlib import pyplot as plt
from celluloid import Camera
import os, sys, subprocess

class PlotUtils:

    fig,ax = plt.subplots()
    camera = Camera(fig)
    filename = 'pso.gif'

    @staticmethod
    def plot_particle(particle):
        plt.scatter(particle.position[0], particle.position[1])

    @staticmethod
    def plot_iteration(bounds,i):
        plt.xlabel('x[0]')
        plt.ylabel('x[1]')
        plt.xlim(bounds[0])
        plt.ylim(bounds[1])
        PlotUtils.ax.text(0.42, 1.01, f'iteration # {i}', transform=PlotUtils.ax.transAxes)
        PlotUtils.camera.snap()

    @staticmethod
    def save():
        animation = PlotUtils.camera.animate(interval=150, blit=True)
        animation.save(PlotUtils.filename, dpi=150)

    @staticmethod
    def play():
        if sys.platform == "win32":
            os.startfile(PlotUtils.filename)
        else:
            opener ="open" if sys.platform == "darwin" else "xdg-open"
            subprocess.call([opener, PlotUtils.filename])
