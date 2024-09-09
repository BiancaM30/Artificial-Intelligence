from sklearn.linear_model import SGDClassifier
from sklearn.metrics import accuracy_score


class ServiceEmoji:
    def __init__(self, train_inputs, train_output, test_inputs, test_output):
        self.train_inputs = train_inputs
        self.train_outputs = train_output
        self.test_inputs = test_inputs
        self.test_outputs = test_output

    def stochastic_gradient_descent(self):
        classifier = SGDClassifier(max_iter=1000)
        classifier.fit(self.train_inputs, self.train_outputs)
        computed = classifier.predict(self.test_inputs)
        accuracy = accuracy_score(self.test_outputs, computed)
        return accuracy


    def run(self):
        accuracy = self.stochastic_gradient_descent()
        print("1.Emoji Acuracy: " + str(accuracy))