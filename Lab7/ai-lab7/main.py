import numpy as np
from manualRegression import ManualRegression
from reader import Reader
from toolRegression import ToolRegression

if __name__ == '__main__':
    inputs, output = Reader('data/v3_world-happiness-report-2017.csv').read(['Economy..GDP.per.Capita.', 'Freedom'],
                                                                            'Happiness.Score')


    # Split the Data Into Training and Test Subsets
    indexes = [i for i in range(len(inputs))]
    trainSample = np.random.choice(indexes, int(0.8 * len(inputs)), replace=False)
    validationSample = [i for i in indexes if not i in trainSample]
    trainInputs = [inputs[i] for i in trainSample]
    trainOutput = [output[i] for i in trainSample]
    validationInputs = [inputs[i] for i in validationSample]
    validationOutput = [output[i] for i in validationSample]


    print('\nSklearn Tool')
    tool_regressor = ToolRegression(trainInputs, trainOutput, validationInputs, validationOutput)
    regressor, w0, w1, w2 = tool_regressor.calculateRegressor()
    print('The learnt model is: f(x) = ', w0, ' + ', w1, ' * x1', ' + ', w2, ' * x2')
    error = tool_regressor.calculateError(regressor)
    print('Prediction error (tool):  ', error)

    print('\n\nManual Tool')
    manual_regressor = ManualRegression(trainInputs, trainOutput, validationInputs, validationOutput)
    regressor, w0, w1, w2 = manual_regressor.calculateRegressor()
    print('The learnt model is: f(x) = ', w0, ' + ', w1, ' * x1', ' + ', w2, ' * x2')
    error = manual_regressor.calculateError(regressor)
    print('Prediction error (tool):  ', error)


