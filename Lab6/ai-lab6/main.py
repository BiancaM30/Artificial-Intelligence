import regression
from classification import Classification
from loss import Loss
from reader import Reader
from regression import Regression


def main():
    realOutputs, computedOutputs = Reader('data/sport.csv').read_regression(['Weight', 'Waist', 'Pulse'],
                                                                            ['PredictedWeight', 'PredictedWaist',
                                                                             'PredictedPulse'])
    regression = Regression(realOutputs, computedOutputs)
    print("\n1. Multi-Target Regression:")
    print(" Mean Absolute Error: " + str(sum(regression.mean_abs_error())))
    print(" Root Mean Square Error: " + str(sum(regression.root_mean_square_error())))

    ################################################################################################
    print('\n\n2.Multi-class classification')
    labelNames = ['Daisy', 'Tulip', 'Rose']
    realLabels, computedLabels = Reader('data/flowers.csv').read_classification()
    classification = Classification(realLabels, computedLabels, labelNames)
    TP, FP, TN, FN = classification.eval()
    print(' Accuracy: ' + str(classification.accuracy()))
    print(' Precision: ' + str(classification.precission(TP, FP)))
    print(' Recall: ' + str(classification.recall(TP, FN)))

    print("\n3. Loss Functions")
    loss = Loss()
    print("Regression loss:" + str(loss.regression()))
    l = loss.binary_classification_loss()
    print("Binary classification " + str(l))

    l = loss.multi_class_loss()
    print("Multi class loss: " + str(l))

    l = loss.multi_label_loss()
    print("Multi label loss: " + str(l))

if __name__ == '__main__':
    main()
