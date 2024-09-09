import numpy as np

from reader import Reader
from service import Service
from utils import normalisation


def main():
    inputs, output, outputNames = Reader().loadIrisData()

    # Split the Data Into Training and Test Subsets 80/20
    indexes = [i for i in range(len(inputs))]
    trainSample = np.random.choice(indexes, int(0.8 * len(inputs)), replace=False)
    testSample = [i for i in indexes if not i in trainSample]

    trainInputs = [inputs[i] for i in trainSample]
    trainOutputs = [output[i] for i in trainSample]
    testInputs = [inputs[i] for i in testSample]
    testOutputs = [output[i] for i in testSample]

    # Normalize the features
    trainInputsNormalized, testInputsNormalized = normalisation(trainInputs, testInputs)

    print(trainInputsNormalized)
    service = Service(trainInputsNormalized, trainOutputs, testInputsNormalized, testOutputs, outputNames)

    print("\n Manual Classifier")
    predictions = service.manual_Classifier()
    print("Accuracy: ", service.accuracy(predictions))


if __name__ == '__main__':
    main()
