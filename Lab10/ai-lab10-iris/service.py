import numpy as np
from sklearn import neural_network
from sklearn.metrics import classification_report
from sklearn.neural_network import MLPClassifier

from ann import MyNetwork


class Service:
    def __init__(self, train_inputs, train_output, test_inputs, test_output, output_names):
        self.train_inputs = train_inputs
        self.train_outputs = train_output
        self.test_inputs = test_inputs
        self.test_outputs = test_output
        self.output_names = output_names

    def accuracy(self, computed):
        return sum([1 if computed[i] == self.test_outputs[i] else 0 for i in range(0, len(
            self.test_outputs))]) / len(self.test_outputs)






    def manual_Classifier(self):
        classifier = MyNetwork(2, 3, (2, 2))
        classifier.fit(self.train_inputs, self.train_outputs)
        predictions = classifier.predict(self.test_inputs)
        return predictions
        self.eval_classification(predictions)




