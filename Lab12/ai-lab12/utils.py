import glob

import cv2
import numpy as np


def getPixelsFromImage(fileName):
    image = cv2.imread(fileName)
    image = image.transpose((2, 0, 1))
    image = image.reshape(image.shape[0], (image.shape[1] * image.shape[2]))
    image = flatten(image)
    return image

def flatten(mat):
    x = []
    for line in mat:
        for el in line:
            el = el / 255
            x.append(el)
    return x




def read_images_emotions():
    path = 'data/facialEmotions/test/'
    emotions = ['angry', 'disgust', 'fear', 'happy', 'neutral', 'sad', 'surprise']
    image_list = []
    for emo in emotions:
        fullpath = path + emo + '/*.jpg'
        size = 0
        emolist = []
        for fileName in glob.glob(fullpath):
            print(fileName)
            size += 1
            image = cv2.imread(fileName)
            image = cv2.resize(image, (48, 48))
            image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            image = np.reshape(image, [1, image.shape[0], image.shape[1], 1])
            emolist.append(image)
            # image = plt.imread(fileName)
            # emolist.append(fileName)
            if size == 50:
                break
        image_list.append(emolist)
    return image_list

