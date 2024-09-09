import random
from math import sqrt, floor


def euclidian_distance(a, b):
    return sqrt(sum([(a[i] - b[i]) ** 2 for i in range(len(a))]))


class ServiceIris:
    def __init__(self, train_inputs, train_output, test_inputs, test_output, output_names):
        self.train_inputs = train_inputs
        self.train_outputs = train_output
        self.test_inputs = test_inputs
        self.test_outputs = test_output
        self.output_names = output_names

    def accuracy(self, computed):
        return sum([1 if computed[i] == self.test_outputs[i] else 0 for i in range(0, len(
            self.test_outputs))]) / len(self.test_outputs)

    def init_centroids(self):
        # calculate the sum of features for every train input
        sums = [sum([i[j] for j in range(4)]) for i in self.train_inputs]
        sorted = sums.copy()
        sorted.sort()

        # split in 3 intervals with same length and choose 3 random indexes
        val = floor(len(sorted) / 3)
        random1 = random.sample(range(0, val), 1)[0]
        random2 = random.sample(range(val + 1, val * 2), 1)[0]
        random3 = random.sample(range(val * 2 + 1, len(sorted) - 1), 1)[0]

        centroids = [self.train_inputs[sums.index(sorted[random1])],
                     self.train_inputs[sums.index(sorted[random2])],
                     self.train_inputs[sums.index(sorted[random3])]
                     ]
        return centroids

    def train(self):
        centroids = self.init_centroids()
        # # kmeans training
        for iteration in range(100):
            # assign to clusters
            clusters = [[0 for _ in range(4)] for _ in range(3)]
            clusters_count = [0, 0, 0]
            for i in self.train_inputs:
                distances = []
                for j in range(3):
                    distances.append(euclidian_distance(centroids[j], i))
                nearest_cluster = distances.index(min(distances))
                clusters[nearest_cluster] = [sum(x) for x in zip(clusters[nearest_cluster], i)]
                clusters_count[nearest_cluster] += 1
            # # reassign centroids
            centroids = [[x / clusters_count[i] for x in clusters[i] if clusters_count[i] != 0] for i in range(3)]

        return centroids

    def predict(self, centroids):
        computed = []
        for i in self.test_inputs:
            distances = [euclidian_distance(centroids[j], i) for j in range(3)]
            nearest_cluster = distances.index(min(distances))
            computed.append(nearest_cluster)
        return computed

    def mean_square_error(self, real, computed):
        rmse = []
        for i in range(len(computed)):
            r = [real[i]]
            c = [computed[i]]
            val = sum([(r[i] - c[i]) ** 2 for i in range(len(c))]) / len(c)
            rmse.append(val)
        return sum([i for i in rmse]) / len(rmse)


    def run(self):
        centroids = self.train()
        computed = self.predict(centroids)
        mae = self.mean_square_error(self.test_outputs, computed)
        accuracy = self.accuracy(computed)
        print("Mean square error: " + str(mae))
        print("Accuracy: " + str(accuracy))
