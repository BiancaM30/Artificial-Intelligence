import np as np

from reader import Reader
from service import Service
from utils import apply_normalization, apply_normalization_multi

if __name__ == '__main__':
    inputs, outputs = Reader('data/world-happiness-report-2017.csv').read(['Economy..GDP.per.Capita.', 'Freedom'],
                                                                        ['Happiness.Score','Family'])

    # Split the Data Into Training and Test Subsets
    indexes = [i for i in range(len(inputs))]
    trainSample = np.random.choice(indexes, int(0.8 * len(inputs)), replace=False)
    testSample = [i for i in indexes if not i in trainSample]

    trainInputs = [inputs[i] for i in trainSample]
    testInputs = [inputs[i] for i in testSample]

    # # single target output
    trainOutput = [outputs[i][0] for i in trainSample]
    testOutput = [outputs[i][0] for i in testSample]

    # # multi target output
    trainOutputsMulti = [outputs[i] for i in trainSample]
    testOutputsMulti = [outputs[i] for i in testSample]


    # # Normalization
    trainInputNormalized, testInputNormalized, trainOutputNormalized, testOutputNormalized = apply_normalization(trainInputs, testInputs, trainOutput, testOutput)
    trainOutputsMultiNormalized, testOutputsMultiNormalized = apply_normalization_multi(trainOutputsMulti, testOutputsMulti)

    service = Service(trainInputNormalized, trainOutputNormalized, testInputNormalized, testOutputNormalized, trainOutputsMultiNormalized, testOutputsMultiNormalized)

    print("\n1. Predictia gradului de fericire in functie doar de Produsul intern brut")
    print("  1.1. Univariate regression using Sklearn Tool")
    service.univariate_regression_tool()
    print("\n  1.2. Univariate regression manual")
    service.univariate_regression_manual()

    print("\n2. Predictia gradului de fericire in functie de Produsul intern brut si gradul de libertate")
    print("\n  2.1. Bivariate Regression using Sklearn Tool")
    service.bivariate_regression_tool()
    print("\n 2.2. Bivariate Regression manual")
    service.bivariate_regression_manual()

    print("\n3. Predictia gradului de fericire si a sperantei de viata in functie de Produsul intern brut si gradul de libertate")
    print("  3.1. Multi Target Regression manual")
    service.multi_target_regression_manual()


