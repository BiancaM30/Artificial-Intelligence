import numpy as np
from keras.api.keras import datasets

from generator import Generator
from service import Service
from utils import normalisation


def main():
    gen = Generator()
    image_list = gen.generateImages()
    inputs, output, outputNames = gen.loadData(image_list)

    # # # Split the Data Into Training and Test Subsets 80/20
    indexes = [i for i in range(len(inputs))]
    trainSample = np.random.choice(indexes, int(0.8 * len(inputs)), replace=False)
    testSample = [i for i in indexes if not i in trainSample]

    trainInputs = [inputs[i] for i in trainSample]
    trainOutputs = [output[i] for i in trainSample]
    testInputs = [inputs[i] for i in testSample]
    testOutputs = [output[i] for i in testSample]

    print("\n 1. Tool Classifier CNN")
    service2 = Service(trainInputs, trainOutputs, testInputs, testOutputs, outputNames)
    service2.tool_CNN()


if __name__ == '__main__':
    main()
