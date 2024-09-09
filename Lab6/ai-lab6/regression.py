from math import sqrt
import matplotlib.pyplot as plt
import numpy as np


class Regression:

    def __init__(self, real, computed):
        self.realOutputs = real
        self.computedOutputs = computed

    def mean_abs_error(self):
        error = []
        i = 0
        while i < len(self.realOutputs):
            error.append(
                sum(abs(real - computed) for real, computed in
                    zip(self.realOutputs[i], self.computedOutputs[i])) / len(
                    self.realOutputs[0]))
            i += 1
        return error

    def root_mean_square_error(self):
        error = []
        i = 0
        while i < len(self.realOutputs):
            error.append(sqrt(
                sum(((real - computed) ** 2) for real, computed in
                    zip(self.realOutputs[i], self.computedOutputs[i])) / len(
                    self.realOutputs[0])))
            i += 1
        return error
