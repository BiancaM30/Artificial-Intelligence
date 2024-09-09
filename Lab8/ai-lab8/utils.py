
# map the feature's values to [0,1]
def scale01(features):
    minFeat = min(features)
    maxFeat = max(features)
    scaledFeatures = [(feat - minFeat) / (maxFeat - minFeat) for feat in features]
    return scaledFeatures


def apply_normalization(trainInput, testInput, trainOutput, testOutput):
    FirstFeature_TrainInputs = scale01([trainInput[i][0] for i in range(len(trainInput))])
    FirstFeature_TestInputs = scale01([testInput[i][0] for i in range(len(testInput))])
    SecondFeature_TrainInputs = scale01([trainInput[i][1] for i in range(len(trainInput))])
    SecondFeature_TestInputs = scale01([testInput[i][1] for i in range(len(testInput))])

    trainInputN = [[FirstFeature_TrainInputs[i], SecondFeature_TrainInputs[i]] for i in
                   range(0, len(FirstFeature_TrainInputs))]
    testInputN = [[FirstFeature_TestInputs[i], SecondFeature_TestInputs[i]] for i in
                  range(0, len(FirstFeature_TestInputs))]
    trainOutputN = scale01(trainOutput)
    testOutputN = scale01(testOutput)

    return trainInputN, testInputN, trainOutputN, testOutputN

def apply_normalization_multi(trainOutputsMulti, testOutputsMulti):
    FirstFeature_TrainOutputs = scale01([trainOutputsMulti[i][0] for i in range(len(trainOutputsMulti))])
    FirstFeature_TestOutputs = scale01([testOutputsMulti[i][0] for i in range(len(testOutputsMulti))])
    SecondFeature_TrainOutputs = scale01([trainOutputsMulti[i][1] for i in range(len(trainOutputsMulti))])
    SecondFeature_TestOutputs = scale01([testOutputsMulti[i][1] for i in range(len(testOutputsMulti))])

    trainOutputsN = [[FirstFeature_TrainOutputs[i], SecondFeature_TrainOutputs[i]] for i in
                   range(0, len(FirstFeature_TrainOutputs))]
    testOutputsN = [[FirstFeature_TestOutputs[i], SecondFeature_TestOutputs[i]] for i in
                  range(0, len(FirstFeature_TestOutputs))]

    return trainOutputsN, testOutputsN