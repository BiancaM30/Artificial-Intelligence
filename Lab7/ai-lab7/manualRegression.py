from sklearn import linear_model
from sklearn.metrics import mean_squared_error

from regression import Regression


class ManualRegression:
    def __init__(self, trainInputs, trainOutputs, testInputs, testOutput):
        self.trainInputs = trainInputs
        self.trainOutput = trainOutputs
        self.testInputs = testInputs
        self.testOutput = testOutput


    def calculateRegressor(self):
        regressor = Regression()
        regressor.fit(self.trainInputs, self.trainOutput)
        w0, w1, w2 = regressor.intercept_, regressor.coef_[0], regressor.coef_[1]
        return regressor, w0, w1, w2

    def calculateError(self, regressor):
        return regressor.meanSquareError(self.testInputs, self.testOutput)
