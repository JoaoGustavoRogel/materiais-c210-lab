import os, sys
import numpy as np
from numpy import append, genfromtxt

class DataSets:

    @staticmethod
    def read(folder, filename):
        filename_abs = os.path.join(os.path.dirname(__file__), folder, filename)
        return genfromtxt(filename_abs, delimiter=",", dtype=float)

    @staticmethod
    def add_bias(arr, bias = -1):
        biased_arr = np.ndarray(shape=(arr.shape[0], arr.shape[1]+1), dtype=float)
        for i in range(0, len(arr)):
            biased_arr[i] = np.append(bias, arr[i])

        return biased_arr


class LOGIC_GATE_AND:
    input = DataSets.add_bias(DataSets.read("logic-gate-and", "input.txt"))
    output = DataSets.read("logic-gate-and", "output.txt")


class LOGIC_GATE_OR:
    input = DataSets.add_bias(DataSets.read("logic-gate-or", "input.txt"))
    output = DataSets.read("logic-gate-or", "output.txt")


class LOGIC_GATE_XOR:
    input = DataSets.add_bias(DataSets.read("logic-gate-xor", "input.txt"))
    output = DataSets.read("logic-gate-xor", "output.txt")


class DIABETES:
    input = DataSets.add_bias(DataSets.read('diabetes', 'input.txt'))
    output = DataSets.read('diabetes', 'output.txt')


class TIC_TAC_TOE_ENDGAME:
    input = DataSets.add_bias(DataSets.read('tic-tac-toe-endgame', 'input.txt'))
    output = DataSets.read('tic-tac-toe-endgame', 'output.txt')

class TESTE:
    input = DataSets.add_bias(DataSets.read('teste', 'input.txt'))
    output = DataSets.read('teste', 'output.txt')
