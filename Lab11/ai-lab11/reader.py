import numpy as np
from PIL import Image
from sklearn.datasets import load_iris


class Reader:
    def __init__(self):
        self.__inputs = []
        self.__outputs = []
        self.__output_names = []

    def loadIrisData(self):
        data = load_iris()
        self.__inputs = data['data']
        self.__outputs = data['target']
        self.__outputNames = data['target_names']
        featureNames = list(data['feature_names'])
        feature1 = [feat[featureNames.index('sepal length (cm)')] for feat in self.__inputs]
        feature2 = [feat[featureNames.index('petal length (cm)')] for feat in self.__inputs]
        feature3 = [feat[featureNames.index('sepal width (cm)')] for feat in self.__inputs]
        feature4 = [feat[featureNames.index('petal width (cm)')] for feat in self.__inputs]
        self.__inputs = [[feat[featureNames.index('sepal length (cm)')], feat[featureNames.index('petal length (cm)')],
                          feat[featureNames.index('sepal width (cm)')], feat[featureNames.index('petal width (cm)')]] for
                  feat in self.__inputs]
        return self.__inputs, self.__outputs, self.__outputNames
