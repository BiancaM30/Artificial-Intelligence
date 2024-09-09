import math

from sklearn.metrics import log_loss


class Loss:

    # Mean absolute error/L1 loss
    def regression(self):
        realOutputs = [7.53, 7.52, 7.5, 7.49, 7.46]
        computedOutputs = [7.8, 7.75, 7.45, 7.6, 7.4]

        cost = sum(abs(r - c) for r, c in zip(realOutputs, computedOutputs)) / len(realOutputs)
        return cost

    # Cross-entropy loss
    def binary_classification_loss(self):
        realLabels = ["ant", "bee", "bee", "ant", "bee"]
        computedOutputs = [[0.4, 0.6], [0.7, 0.3], [0.5, 0.5], [0.4, 0.6], [0.3, 0.7]]

        # suppose that 'ant' is the positive class
        realOutputs = [[1, 0] if label == 'ant' else [0, 1] for label in realLabels]
        datasetSize = len(realLabels)
        noClasses = len(set(realLabels))
        datasetCE = 0.0
        for i in range(datasetSize):
            sampleCE = - sum([realOutputs[i][j] * math.log(computedOutputs[i][j]) for j in range(noClasses)])
            datasetCE += sampleCE
        meanCE = datasetCE / datasetSize

        return meanCE

    def evalSoftmaxCEsample(self, targetValues, rawOutputs):
        # apply softmax for all raw outputs
        noClasses = len(targetValues)
        expValues = [math.exp(val) for val in rawOutputs]
        sumExpVal = sum(expValues)
        mapOutputs = [val / sumExpVal for val in expValues]
        sampleCE = - sum([targetValues[j] * math.log(mapOutputs[j]) for j in range(noClasses)])
        return sampleCE

    # Cross-entropy loss
    def multi_class_loss(self):
        realLabels = [1, 0, 0, 0, 0]
        # realLabels = ["ant", "bee", "wasp", "ant", "wasp"]
        computedOutputs = [[7, 0.2, 2.1, -0.3, -0.1], [0.5, 3, -0.5, 0.9, 0.1], [0.3, 0.4, 0.3, -0.1, 0.6],
                           [-0.1, -0.8, 0.1, 0.2, 0.3], [3, 0.1, -0.2, -0.1, 4]]
        targetValues = [[1, 0, 0, 0, 0], [0, 0, 0, 1, 0], [1, 0, 0, 0, 1], [0, 1, 0, 0, 0], [0, 0, 0, 0, 1]]

        noClasses = len(realLabels)
        datasetSize = len(realLabels)
        datasetCE = 0.0
        # apply softmax for all computed outputs
        for i in range(datasetSize):
            sampleCE = self.evalSoftmaxCEsample(targetValues[i], computedOutputs[i])
            CE = - sum([targetValues[i][j] * math.log(sampleCE) for j in range(noClasses)])
            datasetCE += CE
        meanCE = datasetCE / datasetSize
        return meanCE

    def evalSigmoidCEsample(self, targetValues, rawOutputs):
        # apply softmax for all raw outputs
        noClasses = len(targetValues)
        mapOutputs = [1 / (1 + math.exp(-val)) for val in rawOutputs]
        sampleCE = - sum([targetValues[j] * math.log(mapOutputs[j]) for j in range(noClasses)])
        return sampleCE

    # Cross-entropy loss
    def multi_label_loss(self):
        realLabels = [0, 1, 1, 0, 0]
        computedOutputs = [[1.2, 0.2, 2.3, 0.1, -0.5], [-0.1, -0.6, 0.7, 0.8, 0.2], [0.5, 0.1, 0.5, 0.8, 0.1],
                           [-0.4, -0.2, 0.5, 0.7, 0.2], [0.3, 0.5, 0.7, -0.5, -0.3]]
        targetValues = [[1, 0, 1, 0, 0], [0, 0, 1, 1, 0], [1, 1, 0, 0, 0], [0, 0, 1, 0, 1], [0, 1, 1, 0, 0]]

        noClasses = len(realLabels)
        datasetSize = len(realLabels)
        datasetCE = 0.0
        # apply softmax for all computed outputs
        for i in range(datasetSize):
            sampleCE = self.evalSigmoidCEsample(targetValues[i], computedOutputs[i])
            CE = - sum([targetValues[i][j] * math.log(sampleCE) for j in range(noClasses)])
            datasetCE += CE
        meanCE = datasetCE / datasetSize

        return meanCE
