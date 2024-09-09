import sklearn
from sklearn import linear_model
from sklearn.metrics import mean_squared_error

from MultiTragetRegression import MultiTargetRegression
from MyRegression import MyRegression


class Service:
    def __init__(self, train_inputs, train_output, test_inputs, test_output, train_outputs_multi, test_outputs_multi):
        self.train_inputs = train_inputs
        self.train_output = train_output
        self.test_inputs = test_inputs
        self.test_output = test_output
        self.train_outputs_multi = train_outputs_multi
        self.test_outputs_multi = test_outputs_multi

    def univariate_regression_tool(self):
        train_inputs = [[self.train_inputs[i][0]] for i in range(len(self.train_inputs))]
        test_inputs = [[self.train_inputs[i][0]] for i in range(len(self.test_inputs))]

        regressor = linear_model.SGDRegressor(alpha=0.001, max_iter=1000, average=len(self.train_inputs))

        regressor.fit(train_inputs, self.train_output)
        w0, w1 = regressor.intercept_[0], regressor.coef_[0]
        print("Learnt model is: f(x) = " + str(w0) + " + " + str(w1) + " * x")

        print("ERROR:   ", mean_squared_error(self.test_output, regressor.predict(test_inputs)))

    def univariate_regression_manual(self):
        train_inputs = [[self.train_inputs[i][0]] for i in range(len(self.train_inputs))]
        test_inputs = [[self.train_inputs[i][0]] for i in range(len(self.test_inputs))]

        regressor = MyRegression()
        regressor.fit(train_inputs, self.train_output)
        w0, w1 = regressor.intercept, regressor.coef_[0]
        print('Learnt model is: f(x) = ', w0, ' + ', w1, ' * x')
        print("ERROR: ", regressor.mean_square_error(test_inputs, self.test_output))

    def bivariate_regression_tool(self):
        regressor = linear_model.SGDRegressor(alpha=0.01, max_iter=100, average=len(self.train_inputs))
        regressor.fit(self.train_inputs, self.train_output)
        w0, w1, w2 = regressor.intercept_[0], regressor.coef_[0], regressor.coef_[1]
        print('The learnt model is: f(x) = ', w0, ' + ', w1, ' * x1', ' + ', w2, ' * x2')

        print("ERROR:    ",
              mean_squared_error(self.test_output, regressor.predict(self.test_inputs)))

    def bivariate_regression_manual(self):
        regressor = MyRegression()
        regressor.fit(self.train_inputs, self.train_output)
        w0, w1, w2 = regressor.intercept, regressor.coef_[0], regressor.coef_[1]
        print('The learnt model is: f(x) = ', w0, ' + ', w1, ' * x1', ' + ', w2, ' * x2')

        print("ERROR:  ", regressor.mean_square_error(self.test_inputs, self.test_output))

    def multi_target_regression_manual(self):
        regressor = MultiTargetRegression()
        regressor.fit(self.train_inputs, self.train_outputs_multi)
        w0, w1, w2 = regressor.intercept_, regressor.coef_[0], regressor.coef_[1]
        print('The learnt model is:\nf1(x) = ', w0[0], ' + ', w1[0], ' * x1', ' + ', w2[0], ' * x2\nf2(x) = ', w0[1],
              ' + ', w1[1], ' * x1', ' + ', w2[1], ' * x2')

        print("ERROR:  ", regressor.mean_square_error(self.test_inputs, self.test_outputs_multi))