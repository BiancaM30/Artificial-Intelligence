import np as np

from reader import Reader
from service import Service
from utils import normalisation
import random


def main():
    inputs, output = Reader('iris.data').read()

    # Split the Data Into Training and Test Subsets
    # Hold - out cross - validation
    indexes = [i for i in range(len(inputs))]
    trainSample = np.random.choice(indexes, int(0.8 * len(inputs)), replace=False)
    testSample = [i for i in indexes if not i in trainSample]

    trainInputs = [inputs[i] for i in trainSample]
    testInputs = [inputs[i] for i in testSample]

    trainOutput = [output[i] for i in trainSample]
    testOutput = [output[i] for i in testSample]

    # Normalize the features
    trainInputsNormalized, testInputsNormalized = normalisation(trainInputs, testInputs)

    service = Service(trainInputsNormalized, trainOutput, testInputsNormalized, testOutput)

    print("\n 1. Logistic regression using tool")
    service.logistic_regression_tool()

    print("\n 2. Manual Logistic regression")
    accuracy, loss = service.logistic_regression_manual()
    print("\nAccuracy: ", accuracy)
    print('\nLoss: ', loss)

    print("\n 3. Manual Logistic regression using k-fold cross validation")
    k = 10  # number of folds
    indexes = [i for i in range(len(inputs))]
    random.shuffle(indexes)
    nrElemsPerFold = int(len(inputs) / k)
    poz = 0
    folds = [[] for i in range(k)]
    for i in range(0, k):
        for j in range(poz, poz + nrElemsPerFold):
            folds[i].append(indexes[j])
        poz += nrElemsPerFold

    accuracies = [0 for i in range(k)]
    loss = [0 for i in range(k)]
    for poz in range(0, k):  # Choose k – 1 folds as the training set. The remaining fold will be the test set
        testSample = folds[poz]
        trainSample = [i for i in indexes if not i in testSample]

        trainInputs = [inputs[i] for i in trainSample]
        testInputs = [inputs[i] for i in testSample]

        trainOutput = [output[i] for i in trainSample]
        testOutput = [output[i] for i in testSample]

        trainInputsNormalized, testInputsNormalized = normalisation(trainInputs, testInputs)
        serviceKFold = Service(trainInputsNormalized, trainOutput, testInputsNormalized,
                               testOutput)  # Validate on the test set
        accuracies[poz], loss[poz] = serviceKFold.logistic_regression_manual()  # Save the result of the validation

    # get the final score average the results
    print("Average accuracy: ", sum(accuracies) / len(accuracies))
    print("Average loss: ", sum(loss) / len(loss))

if __name__ == '__main__':
    main()
