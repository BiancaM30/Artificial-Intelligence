import random

import numpy as np

# Transfer neuron activation
def sigmoid(x):
    return 1 / (1 + np.exp(-x))


def der(x):
    return x * (1 - x)


def softmax(y):
    exp = [np.exp(i) for i in y]
    s = sum(exp)
    return [i / s for i in exp]


class MyNetwork:
    def __init__(self, nr_input_nodes, nr_output_nodes, hidden_layers=2, learning_rate=0.001, iterations=100):
        self.nr_input_nodes = nr_input_nodes
        self.nr_output_nodes = nr_output_nodes
        self.hidden_layers = hidden_layers
        self.learning_rate = learning_rate
        self.iterations = iterations

        self.init_weights()
        self.init_biases()

    def init_weights(self):
        self.weights = []
        # edge from input layer to first hidden layer
        self.weights.append(np.random.rand(self.hidden_layers[0], self.nr_input_nodes))
        # edges between hidden layers
        for i in range(1, len(self.hidden_layers)):
            row = np.random.rand(self.hidden_layers[i], self.hidden_layers[i - 1])
            self.weights.append(row)
        # edges between last hidden layer and output layer
        self.weights.append(np.random.rand(self.nr_output_nodes, self.hidden_layers[len(self.hidden_layers) - 1]))

    def init_biases(self):
        # edge from input layer to first hidden layer
        self.biases = []
        self.biases.append(np.random.rand(self.hidden_layers[0], 1))
        # edges between hidden layers
        for i in range(1, len(self.hidden_layers)):
            bias = np.random.rand(self.hidden_layers[i], 1)
            self.biases.append(bias)
        # edges between last hidden layer and output layer
        self.biases.append(np.random.rand(self.nr_output_nodes, 1))

    def fit(self, train_inputs, train_outputs):
        indexes = [i for i in range(len(train_inputs))]
        for i in range(self.iterations):
            indexes_shuffled = random.sample(indexes, len(indexes))  # shuffle train data
            train_sample_inputs = [train_inputs[i] for i in indexes_shuffled]
            train_sample_outputs = [train_outputs[i] for i in indexes_shuffled]

            # train the network
            for j in range(len(train_sample_inputs)):
                self.train(train_sample_inputs[j], train_sample_outputs[j])

            current_error = self.mean_square_error(train_sample_outputs, self.predict_probab(train_sample_inputs))
            print("Iteration {} error: {}".format(i, current_error))

    def train(self, inputs, outputs):
        # forward propagation
        input_mat = np.array(inputs)
        layer_results = []
        layer_input = input_mat.reshape((input_mat.shape[0], 1))
        input_mat = layer_input
        for i in range(len(self.weights)):
            mat = self.weights[i]
            bias = self.biases[i]
            result_mat = mat.dot(layer_input)
            result_mat = result_mat + bias
            if i != len(self.weights) - 1:
                result_mat = self.activate(sigmoid, result_mat)
            else:
                result_mat = np.array(softmax(result_mat.flatten()))
                result_mat = result_mat.reshape((result_mat.shape[0], 1))
            layer_input = result_mat
            layer_results.append(result_mat)
        predicted = layer_input.flatten()  # will contain the probability for each of the 3 flowers

        # error
        out = np.array(outputs)
        layer_error = predicted - out
        layer_error = layer_error.reshape((layer_error.shape[0], 1))

        # backpropagation
        errors = self.compute_errors(layer_error)
        self.update_weights(errors, layer_results, input_mat)


    def activate(self, func, mat):
        vfunc = np.vectorize(func)
        return vfunc(mat)

    def compute_errors(self, layer_error):
        errors = []
        layer_nr = len(self.weights)
        for i in range(layer_nr - 1, -1, -1):
            error_index = layer_nr - 1 - i
            # compute layer error
            if i == layer_nr - 1:
                errors.append(layer_error)
            else:
                tran = self.weights[i + 1].transpose()
                errors.append(tran.dot(errors[error_index - 1]))
        return errors

    def update_weights(self, errors, layer_results, input_mat):
        layer_nr = len(self.weights)
        for i in range(layer_nr - 1, -1, -1):
            error_index = layer_nr - 1 - i
            # update layer weights
            if i == layer_nr - 1:
                gradients = errors[error_index]
            else:
                gradients = self.activate(der, layer_results[i])
                gradients = gradients * errors[error_index]
            gradients = gradients * self.learning_rate
            self.biases[i] = self.biases[i] - gradients
            if i != 0:
                input_tran = layer_results[i - 1].transpose()
            else:
                input_tran = input_mat.transpose()
            gradients = gradients.dot(input_tran)
            self.weights[i] = self.weights[i] - gradients

    def mean_square_error(self, real, computed):
        real_vect = []
        for el in real:
            real_vect.append([0 for i in range(self.nr_output_nodes)])
            real_vect[len(real_vect) - 1][el] = 1

        # compute mae for every flower type
        rmse = []
        for i in range(len(computed[0])):
            r = [real_vect[j][i] for j in range(len(real_vect))]
            c = [computed[j][i] for j in range(len(computed))]
            val = sum([(r[i] - c[i]) ** 2 for i in range(len(c))]) / len(c)
            rmse.append(val)
        return sum([i for i in rmse]) / len(rmse)

    def predict_probab(self, inputs):
        result = []
        for i in range(len(inputs)):
            result.append(self.predict_sample(inputs[i]))
        return result

    def predict_sample(self, inputs_sample):
        input_mat = np.array(inputs_sample)
        layer_input = input_mat.reshape((input_mat.shape[0], 1))
        for i in range(len(self.weights)):
            mat = self.weights[i]
            bias = self.biases[i]
            result_mat = mat.dot(layer_input)
            result_mat = result_mat + bias
            if i == len(self.weights) - 1:
                result_mat = np.array(softmax(result_mat.flatten()))
                result_mat = result_mat.reshape((result_mat.shape[0], 1))
            else:
                result_mat = self.activate(sigmoid, result_mat)
            layer_input = result_mat
        return layer_input.flatten()

    def predict(self, inputs):
        probab = self.predict_probab(inputs)
        results = []
        for i in range(len(probab)):
            index = np.where(probab[i] == (max(probab[i])))[0]
            results.append(index.tolist()[0])
        return results
