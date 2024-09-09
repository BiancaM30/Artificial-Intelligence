from sklearn import linear_model
from sklearn.metrics import mean_squared_error


class ToolRegression:
    def __init__(self, trainInputs, trainOutputs, testInputs, testOutput):
        self.trainInputs = trainInputs
        self.trainOutput = trainOutputs
        self.testInputs = testInputs
        self.testOutput = testOutput

    def calculateRegressor(self):
        # model initialisation
        regressor = linear_model.LinearRegression()
        # training the model by using the training inputs and known training outputs
        regressor.fit(self.trainInputs, self.trainOutput)
        # save the model parameters
        w0, w1, w2 = regressor.intercept_, regressor.coef_[0], regressor.coef_[1]
        return regressor, w0, w1, w2

    def calculateError(self, regressor):
        computedValidationOutputs = regressor.predict(self.testInputs)
        error = mean_squared_error(self.testOutput, computedValidationOutputs)
        return error
