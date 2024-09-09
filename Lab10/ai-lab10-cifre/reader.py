import numpy as np
from PIL import Image
from sklearn.datasets import load_iris, load_digits


class Reader:
    def __init__(self):
        self.__inputs = []
        self.__outputs = []
        self.__output_names = []

    def loadDigitData(self):
        data = load_digits()
        inputs = data.images
        outputs = data['target']
        outputNames = data['target_names']

        # shuffle the original data
        noData = len(inputs)
        permutation = np.random.permutation(noData)
        inputs = inputs[permutation]
        outputs = outputs[permutation]

        return inputs, outputs, outputNames