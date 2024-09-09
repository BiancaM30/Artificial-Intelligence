import numpy as np
from sklearn import linear_model

from myLogisticRegression import MyLogisticRegression


class Service:
    def __init__(self, train_inputs, train_output, test_inputs, test_output):
        self.train_inputs = train_inputs
        self.train_output = train_output
        self.test_inputs = test_inputs
        self.test_output = test_output
        self.folds = []


    def logistic_regression_tool(self):
        classifier = linear_model.LogisticRegression(max_iter=1000)
        classifier.fit(self.train_inputs, self.train_output)

        # w0, w1, w2, w3 = classifier.intercept_, classifier.coef_[0], classifier.coef_[1], classifier.coef_[2]
        # print('classification model: y(feat1, feat2, feat3, feat4) = ', w0, ' + ', w1, ' * feat1 + ', w2, ' * feat2',
        #       w3, ' * feat3')

        predicted_class = classifier.predict(self.test_inputs)

        accuracy = sum([1 if predicted_class[i] == self.test_output[i] else 0 for i in range(0, len(
            self.test_output))]) / len(self.test_output)
        print("\nAccuracy: ", accuracy)

    # Binary Cross Entropy/Log Loss
    @staticmethod
    def cross_entropy_loss(computed_outputs):
        n = len(computed_outputs)
        sum = 0
        for list in computed_outputs:
            sum += np.log(max(list))
        return -1 / n * sum

    def logistic_regression_manual(self):
        labels = ["Iris-setosa", "Iris-versicolor", "Iris-virginica"]
        pred = []
        # one vs all method
        for label in labels:
            classifier = MyLogisticRegression()
            outputs = [1 if self.train_output[i] == label else 0 for i in range(len(self.train_output))]
            classifier.fit(self.train_inputs, outputs)
            pred.append(classifier.predict(self.test_inputs))
        outputs = [[pred[i][j] for i in range(len(pred))] for j in range(len(pred[0]))]

        predicted_class = []

        for i in range(0, len(pred[0])):
            predicted_class.append(labels[outputs[i].index(max(outputs[i]))])

        # print(" Computed label vs Real label")
        # print(predicted_class)
        # print(self.test_output)

        accuracy = sum([1 if predicted_class[i] == self.test_output[i] else 0 for i in range(0, len(
            self.test_output))]) / len(self.test_output)

        return accuracy, self.cross_entropy_loss(outputs)
