class MyRegression:
    def __init__(self):
        self.intercept = 0.0
        self.coef_ = []

    # Batch GD
    # x = inputs, y = real output
    def fit(self, x, y, learning_rate=0.001, no_epochs=1000):
        self.coef_ = [0.0 for _ in range(len(x[0]) + 1)]  # w coefficients y = w0 + w1 * x1 + w2 * x2 + ...
        for epoch in range(no_epochs):
            errors = [0.0 for _ in range(len(x[0]) + 1)]
            for i in range(len(x)):  # for each sample from the training data
                y_computed = self.eval(x[i])  # estimate the output
                crtError = y_computed - y[i]  # compute the error for the current sample
                for j in range(0, len(x[0])): # for every feature from training data we update the error
                    errors[j] += crtError * x[i][j]
                errors[-1] += crtError
            for i in range(0, len(x[0]) + 1):  # update the coefficients at the end of an epoch
                self.coef_[i] -= (learning_rate * (errors[i] / len(x)))

        self.intercept = self.coef_[-1]
        self.coef_ = self.coef_[:-1]

    def eval(self, xi):
        yi = self.coef_[-1]
        for j in range(len(xi)):
            yi += self.coef_[j] * xi[j]
        return yi

    def predict(self, x):
        yComputed = [self.eval(xi) for xi in x]
        return yComputed

    def mean_square_error(self, myinput, myoutput):
        error = 0.0
        for t1, t2 in zip(self.predict(myinput), myoutput):
            error += (t1 - t2) ** 2
        error = error / len(myoutput)
        return error
