import csv


class Reader:
    def __init__(self, filename):
        self.filename = filename

    def loadData(self, inputVariabName, outputVariabName):
        data = []
        dataNames = []
        with open(self.filename) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_line_count = 0
            for row in csv_reader:
                if line_line_count == 0:
                    dataNames = row
                else:
                    data.append(row)
                line_line_count += 1
        selectedVariable = dataNames.index(inputVariabName)
        inputs = [float(data[i][selectedVariable]) for i in range(len(data))]
        selectedOutput = dataNames.index(outputVariabName)
        outputs = [float(data[i][selectedOutput]) for i in range(len(data))]

        return inputs, outputs

    def read(self, inputVariabName, outputVariabName):
        data = []
        dataNames = []
        with open(self.filename) as csv_file:
            reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            for row in reader:
                if line_count == 0:
                    dataNames = row
                else:
                    data.append(row)
                line_count += 1
        selectedVariable = []
        for label in inputVariabName:
            selectedVariable.append(dataNames.index(label))
        inputs = [[float(data[i][j]) for j in selectedVariable] for i in range(len(data))]

        selectedOutput = dataNames.index(outputVariabName)
        outputs = [float(data[i][selectedOutput]) for i in range(len(data))]

        return inputs, outputs