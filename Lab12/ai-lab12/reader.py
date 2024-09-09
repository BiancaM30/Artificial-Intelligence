import csv

class Reader:
    def __init__(self, filename):
        self.filename = filename
        self.__inputs = []
        self.__outputs = []
        self.__output_names = []

    def loadEmoji(self):
        data = []
        with open(self.filename) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            for row in csv_reader:
                if line_count == 0:
                    data_names = row
                else:
                    data.append(row)
                line_count += 1

        inputs_code = [data[i][1].replace("U+", "") for i in range(len(data))]
        outputs = [data[i][3] for i in range(len(data))]

        return inputs_code, outputs
