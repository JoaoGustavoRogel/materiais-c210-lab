import numpy as np
from _data import DataSets
from _math import ActivationFunctions
from _plot import PlotUtils


class Perceptron:
    
    # Learning rate, activation function
    def __init__(self, n, g):
        self.n = n
        self.g = g

        self.plot_data_x = []
        self.plot_data_y = []

    def train(self, x, d):
        k = len(x)
        w = np.random.rand(len(x[0]))

        epoch = 0
        error = True
        while error and epoch < 10000:
            error = False

            for i in range(0, k):
                v = np.dot(np.transpose(w), x[i])
                y = self.g(v)

                if y != d[i]:
                    error = True
                    w = np.add(w, np.multiply(self.n * (d[i] - y), x[i]))

            epoch += 1

            self.plot_data_x.append(epoch)
            self.plot_data_y.append(1 if error else 0)

        return w

    def test(self, w, x):
        v = np.dot(np.transpose(w), x)
        y = self.g(v)
        return y

    def evaluate(self, w, x, d):
        correct = 0
        total = len(x)

        for i in range(0, total):
            y = self.test(w, x[i])
            if y == d[i]:
                correct += 1

        accuracy = (float(correct) / float(total)) * 100.0
        print(f"Accuracy: {accuracy:.2f} -> ({correct}/{total})")

        return accuracy


if __name__ == "__main__":
    np.set_printoptions(formatter={"float": "{: 0.6f}".format})

    # Load data
    x = DataSets.TESTE.input
    d = DataSets.TESTE.output

    # Seting parameters
    n = 0.1
    g = ActivationFunctions.heaviside

    # Creating Neural Network
    nn = Perceptron(n, g)

    # Fitting w
    w = nn.train(x, d)

    # Accuracy
    acc = nn.evaluate(w, x, d)

    # Ploting
    PlotUtils.plot(nn.plot_data_x, "epoch", nn.plot_data_y, "error")
