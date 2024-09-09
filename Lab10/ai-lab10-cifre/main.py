import numpy as np

from reader import Reader
from service import Service
from utils import normalisation


def main():
    inputs_aux, output_aux, outputNames = Reader().loadDigitData()

    output = []
    inputs = []
    for i in range(0, 150):
        inputs.append(inputs_aux[i])
        output.append(output_aux[i])


    # Split the Data Into Training and Test Subsets 80/20
    indexes = [i for i in range(len(inputs))]
    trainSample = np.random.choice(indexes, int(0.8 * len(inputs)), replace=False)
    testSample = [i for i in indexes if not i in trainSample]

    trainInputs = [inputs[i] for i in trainSample]
    trainOutputs = [output[i] for i in trainSample]
    testInputs = [inputs[i] for i in testSample]
    testOutputs = [output[i] for i in testSample]

    # print(testInputs)
    # print(testOutputs)

    def flatten(mat):
        x = []
        for line in mat:
            for el in line:
                x.append(el)
        return x

    trainInputsFlatten = [flatten(el) for el in trainInputs]
    testInputsFlatten = [flatten(el) for el in testInputs]

    #print(len(output))
    #print(testInputsFlatten)
    # # # Normalize the features
    trainInputsNormalized, testInputsNormalized = normalisation(trainInputsFlatten, testInputsFlatten)
    # print(testInputsNormalized)
    # #
    service = Service(trainInputsNormalized, trainOutputs, testInputsNormalized, testOutputs, outputNames)
    #service = Service(trainInputsFlatten, trainOutputs, testInputsFlatten, testOutputs, outputNames)
    #
    #print("\n 1. Tool Classifier")
    #service.tool_MLP_Classifier()
    #
    print("\n 2. Manual Classifier")
    predictions = service.manual_Classifier()
    print("Accuracy: ", service.accuracy(predictions))

if __name__ == '__main__':
    main()
