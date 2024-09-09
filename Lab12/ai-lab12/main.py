import numpy as np

from emotii_faciale import run_facial_emotions
from reader import Reader
from service_emoji import ServiceEmoji
from service_emotions import ServiceEmotions
from utils import getPixelsFromImage


def main():
    inputs, output = Reader("data/faces.csv").loadEmoji()

    # Split the Data Into Training and Test Subsets 80/20
    indexes = [i for i in range(len(inputs))]
    trainSample = np.random.choice(indexes, int(0.8 * len(inputs)), replace=False)
    testSample = [i for i in indexes if not i in trainSample]

    trainInputs = [inputs[i] for i in trainSample]
    trainOutputs = [output[i] for i in trainSample]
    testInputs = [inputs[i] for i in testSample]
    testOutputs = [output[i] for i in testSample]

    # get the pixels as inputs
    for i in range(0, len(trainInputs)):
        trainInputs[i] = getPixelsFromImage("data/emoji_img/" + trainInputs[i]+".jpg")
    for i in range(0, len(testInputs)):
        testInputs[i] = getPixelsFromImage("data/emoji_img/" + testInputs[i]+".jpg")

    # service_emoji = ServiceEmoji(trainInputs, trainOutputs, testInputs, testOutputs)
    # service_emoji.run()


    run_facial_emotions()

if __name__ == '__main__':
    main()
