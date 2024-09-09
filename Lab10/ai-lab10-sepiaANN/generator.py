import glob

from PIL import Image

from imageUtils import save_image, get_pixel
from sepiaUtils import convert_sepia


class Generator:
    def __init__(self):
        self.__inputs = []
        self.__outputs = []
        self.__output_names = []

    # generate one normal image followd by one sepia image
    def generateImages(self):
        image_list = []
        contor = 1
        switch = 0
        for filename in glob.glob(
                'D:/Cursuri facultate sem 4/Inteligenta artificiala/Labs/Lab10/ai-lab10-sepiaANN/dog_dataset//*.jpg'):  # assuming gif
            img = Image.open(filename)
            newsize = (8, 8)
            img1 = img.resize(newsize)
            if (switch == 1):
                switch = 0
                img1 = convert_sepia(img1)
            else:
                switch = 1
            save_image(img1,
                       "D:/Cursuri facultate sem 4/Inteligenta artificiala/Labs/Lab10/ai-lab10-sepiaANN/generatedImg/img" + str(
                           contor) + ".jpg")
            contor += 1
            image_list.append(img1)
        return image_list

    def loadData(self, image_list):
        switch = 0
        inputs = [[] for i in range(0, 200)]
        outputs = []
        for contor in range(0, 200):
            for i in range(0, 8):
                for j in range(0, 8):
                    pixel = get_pixel(image_list[contor], i, j)
                    sum = 0
                    for culoare in pixel:
                        sum += culoare
                    inputs[contor].append(sum/3)
                    if (switch == 1):
                        switch = 0
                        outputs.append(0) #sepia
                    else:
                        outputs.append(1) #normala
                        switch = 1

        outputsNames = ["normala", "sepia"]
        return inputs, outputs, outputsNames
