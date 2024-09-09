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
                'C:/tensorflow/aaa/dog_dataset//*.jpg'):  # assuming gif
            img = Image.open(filename)
            newsize = (32, 32)
            img1 = img.resize(newsize)
            if (switch == 1):
                switch = 0
                img1 = convert_sepia(img1)
            else:
                switch = 1
            save_image(img1,
                       "C:/tensorflow/aaa/generatedImg/img" + str(contor) + ".jpg")
            contor += 1
            image_list.append(img1)
        return image_list

    def loadData(self, image_list):
        switch = 0
        #inputs = [[] for i in range(0, 200)]
        inputs = []
        outputs = []
        for contor in range(0, 200):
            crt_image = []
            for i in range(0, 32):
                crt_row = []
                for j in range(0, 32):
                    pixel = get_pixel(image_list[contor], i, j)
                    crt_row.append(pixel)
                crt_image.append(crt_row)
            inputs.append(crt_image)
            if (switch == 1):
                switch = 0
                outputs.append(0)  # sepia
            else:
                outputs.append(1)  # normala
                switch = 1

        outputsNames = ["normala", "sepia"]
        return inputs, outputs, outputsNames
