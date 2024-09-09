class Reader:
    def __init__(self, filename):
        self.filename = filename

    def read(self):
        file = open(self.filename, 'r')
        inputs = []
        output = []
        Lines = file.readlines()

        for line in Lines:
            features = line.split(",")
            inputs.append([float(features[0]), float(features[1]), float(features[2]), float(features[3])])
            output.append(features[4].split('\n')[0])

        file.close()
        return inputs, output
