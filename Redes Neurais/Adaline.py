import numpy as np
from _data import DataSets
from _math import ActivationFunctions, MathUtils
from _plot import PlotUtils

class Adaline:

    def __init__(self, n, g, e):
        self.n = n # learning rate
        self.g = g # activation function
        self.e = e # error variation tolerance
        self.plot_data_x = [] # epochs for plotting
        self.plot_data_y = [] # eqms for plotting

    def train(self, x, d):
        k = len(x)
        w = np.random.rand(len(x[0]))
        epoch = 0
        while True:
            mse_before = MathUtils.mean_squared_error(w, x, d)
            for i in range(0, k):
                v = np.dot(np.transpose(w), x[i])
                w = np.add(w, np.multiply(x[i], self.n * (d[i] - v)))
            epoch = epoch + 1

            mse_after = MathUtils.mean_squared_error(w, x, d)

            print(f"Epoch: {epoch}\tWeights: {w}\tError: {mse_after:.12f}")

            self.plot_data_x.append(epoch)
            self.plot_data_y.append(mse_after)

            if abs(mse_after - mse_before) <= self.e:
                break
        return w

    def test(self, w, x):
        v = np.dot(np.transpose(w), x)
        y = self.g(v)
        return y
    
    def evaluate(self, w, x, d):
        correct = 0
        total = len(x)
        for i in range(0, len(x)):
            y = self.test(w, x[i])
            if (y == d[i]):
                correct = correct + 1
        accuracy = 100.0 * (float(correct) / float(total))
        print(f"Accuracy: {accuracy:.2f}% ({correct}/{total})")
        return accuracy

if __name__ == "__main__":
    # load data
    x = DataSets.TIC_TAC_TOE_ENDGAME.input
    d = DataSets.TIC_TAC_TOE_ENDGAME.output

    # define the network parameters
    n = 1e-4
    g = ActivationFunctions.heaviside
    e = 1e-10

    # create the neural network
    nn = Adaline(n, g, e)

    # train the neural network
    w = nn.train(x, d)

    # evaluate the neural network
    acc = nn.evaluate(w, x, d)
    
    # plot epoch versus error data
    PlotUtils.plot(nn.plot_data_x, "epoch", nn.plot_data_y, "mse")
