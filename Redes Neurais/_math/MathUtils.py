import numpy as np


def mean_squared_error(w, x, d):
    mse = 0
    for i in range(0,len(x)):
        v = np.dot(np.transpose(w), x[i])
        mse = mse + pow(d[i] - v, 2)
    mse = mse / len(x)
    return mse