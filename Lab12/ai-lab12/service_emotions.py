import numpy as np

from keras.models import load_model

from utils import read_images_emotions


class ServiceEmotions:

    def __init__(self):
        print("a")

    def pretrained(self):
        data = read_images_emotions()
        model = load_model("./emotion_detector_models/model_v6_23.hdf5")
        emotions = ['angry', 'disgust', 'fear', 'happy', 'neutral', 'sad', 'surprise']

        count = 0
        for i in range(len(emotions)):
            print('predicting', emotions[i], '..')
            inputs = data[i]
            for img in inputs:
                predicted = emotions[np.argmax(model.predict(img))]
                print(predicted)
                if predicted == emotions[i]:
                    count += 1
        return count / sum([len(data[i]) for i in range(len(emotions))])

    def run(self):
        accuracy = self.pretrained()
        print("2.Emotions Acuracy: " + str(accuracy))
