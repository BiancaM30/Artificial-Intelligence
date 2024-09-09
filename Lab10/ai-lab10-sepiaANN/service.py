import numpy as np
from sklearn import neural_network
from sklearn.metrics import classification_report



class Service:
    def __init__(self, train_inputs, train_output, test_inputs, test_output, output_names):
        self.train_inputs = train_inputs
        self.train_outputs = train_output
        self.test_inputs = test_inputs
        self.test_outputs = test_output
        self.output_names = output_names


    # ANN
    def tool_MLP_Classifier(self):
        classifier = neural_network.MLPClassifier(hidden_layer_sizes=(2,), activation='relu', max_iter=200,
                                                  solver='sgd', verbose=10, random_state=1, learning_rate_init=.01)
        classifier.fit(self.train_inputs, self.train_outputs)  # training
        predicted_prob = classifier.predict_proba(self.test_inputs)
        predicted_labels = []
        for i in range(len(predicted_prob)):
            index = np.where(predicted_prob[i] == (max(predicted_prob[i])))[0]
            predicted_labels.append(index.tolist()[0])
        print(classification_report(self.test_outputs, predicted_labels))

