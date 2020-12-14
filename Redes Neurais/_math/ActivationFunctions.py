import numpy as np

def heaviside(v):
    if v >= 0:
        return 1
    else:
        return 0

def heaviside_symmetric(v):
    return np.sign(v)