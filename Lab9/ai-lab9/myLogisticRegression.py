from math import exp


def sigmoid(x):
    return 1 / (1 + exp(-x))


class MyLogisticRegression:
    def __init__(self):
        self.intercept_ = 0.0
        self.coef_ = []

    # use the gradient descent method
    # batch GD
    def fit(self, x, y, learningRate=3, noEpochs=1000):  # w coefficients y = w0 + w1 * x1 + w2 * x2 + ...
        self.coef_ = [0.0 for _ in range(len(x[0]) + 1)]
        for epoch in range(noEpochs):
            errors = [0.0 for _ in range(len(x[0]) + 1)]
            for i in range(len(x)):  # for each sample from the training data
                y_computed = sigmoid(self.eval(x[i]))  # estimate the output
                crtError = y_computed - y[i]  # compute the error for the current sample
                for j in range(0, len(x[0])):  # for every feature from training data we update the error
                    errors[j] += crtError * x[i][j]
                errors[-1] += crtError
            for i in range(0, len(x[0]) + 1):  # update the coefficients
                self.coef_[i] -= (learningRate * (errors[i] / len(x)))

        self.intercept_ = self.coef_[-1]
        self.coef_ = self.coef_[:-1]

    def eval(self, xi):
        y = self.coef_[-1]
        for j in range(len(xi)):
            y += self.coef_[j] * xi[j]
        return y

    def predict(self, test_input):
        self.coef_.append(self.intercept_)
        computedLabel = [sigmoid(self.eval(sampleFeatures)) for sampleFeatures in test_input]
        return computedLabel
