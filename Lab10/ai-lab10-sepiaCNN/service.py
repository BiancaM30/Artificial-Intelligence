import tensorflow as tf
from keras.api.keras import datasets
from tensorflow.keras import layers, models
# from tensorflow.keras.models import Sequential
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

    def accuracy(self, computed):
        return sum([1 if computed[i] == self.test_outputs[i] else 0 for i in range(0, len(
            self.test_outputs))]) / len(self.test_outputs)

    # CNN
    def tool_CNN(self):
        model = models.Sequential()
        model.add(layers.Conv2D(32, (3, 3), activation='relu', input_shape=(32, 32, 3)))
        model.add(layers.MaxPooling2D((2, 2)))
        model.add(layers.Conv2D(64, (3, 3), activation='relu'))
        model.add(layers.MaxPooling2D((2, 2)))
        model.add(layers.Conv2D(64, (3, 3), activation='relu'))

        model.add(layers.Flatten())
        model.add(layers.Dense(64, activation='relu'))
        model.add(layers.Dense(10))

        model.summary()

        model.compile(optimizer='adam',
                      loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
                      metrics=['accuracy'])

        history = model.fit(self.train_inputs, self.train_outputs, epochs=10,
                            validation_data=(self.test_inputs, self.test_outputs))
