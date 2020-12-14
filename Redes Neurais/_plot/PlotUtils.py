import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator


def plot(x, _xlabel, y, _ylabel):
    
    if len(x) == 1 and len(y) == 1:
        print("Error in plot!! Len == 1")
    else:
        ax = plt.gca()
        ax.plot(x, y, color="blue", linewidth=1.5)
        ax.xaxis.set_major_locator(MaxNLocator(integer=True))

        ax.set_xlim([np.min(x), np.max(x)])
        ax.set_ylim([np.min(y), np.max(y)])

        ax.set_xlabel(_xlabel)
        ax.set_ylabel(_ylabel)
        ax.set_title(f"{_xlabel} vs {_ylabel}")

        ax.grid()
        plt.show()

