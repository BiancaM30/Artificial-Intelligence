import csv

class Reader:
    def __init__(self, filename):
        self.filename = filename
        self.__inputs = []
        self.__outputs = []
        self.__output_names = []

    def loadReviews(self):
        data = []

        with open(self.filename) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            for row in csv_reader:
                data.append(row)

        data = data[1:]
        inputs = [data[i][0] for i in range(len(data))]
        output = [data[i][1] for i in range(len(data))]
        return inputs, output

