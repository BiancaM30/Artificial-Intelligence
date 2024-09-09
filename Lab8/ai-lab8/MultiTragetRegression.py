class MultiTargetRegression:
    def __init__(self):
        self.coef_ = []
        self.intercept_ = []

    @staticmethod
    def initialize_matrix(x, y):
        intercept_ = []
        coef_ = []
        for i in range(y):
            intercept_.append(0.0)
            row = []
            for j in range(x):
                row.append(0.0)
            coef_.append(row)
        return coef_, intercept_

    def fit(self, x, y):
        learning_rate = 0.001
        no_epochs = 1

        # initialization of intercept and coef
        self.intercept_ = [0.0 for i in range(len(y[0]))]
        self.coef_ = [[] for i in range(len(y[0]))]
        for i in range(len(y[0])):
            for j in range(len(x[0])):
                self.coef_[i].append(0.0)

        for epoch in range(no_epochs):
            errors = self.initialize_matrix(len(x[0]) + 1, len(y[0]))[0]
            for i in range(len(x)):
                y_computed = self.eval(x[i])  # estimate the output
                crtError = [y_computed[j] - y[i][j] for j in
                            range(len(y[0]))]  # compute the error for the current sample
                for k in range(len(y[0])):
                    for j in range(len(x[0])):
                        errors[k][j] += (1 / len(x)) * crtError[k] * x[i][j]
                    errors[k][-1] += (1 / len(x)) * crtError[k]
            for i in range(len(y[0])):
                for j in range(len(x[0])):
                    self.coef_[i][j] -= errors[i][j] * learning_rate
                self.intercept_[i] -= errors[i][-1] * learning_rate
            print(errors)

    def eval(self, x):
        result = []
        for i in range(len(self.intercept_)):
            s = self.intercept_[i]
            for j in range(len(x)):
                s += x[j] * self.coef_[i][j]
            result.append(s)
        return result

    def mean_square_error(self, real, computed):
        mse = []
        for i in range(len(real[0])):
            r = [real[j][i] for j in range(len(real))]
            c = [computed[j][i] for j in range(len(computed))]
            val = sum([(c[i] - r[i]) ** 2 for i in range(len(c))]) / len(c)
            mse.append(val)
        return sum([i for i in mse]) / len(mse)
