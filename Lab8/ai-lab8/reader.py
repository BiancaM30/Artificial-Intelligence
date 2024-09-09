import csv


class Reader:
    def __init__(self, filename):
        self.filename = filename

    def read(self, inputsVariabName, outputsVariabName):
        data = []
        labels = []
        with open(self.filename) as csv_file:
            reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            for row in reader:
                if line_count == 0:
                    labels = row
                else:
                    data.append(row)
                line_count += 1
        selectedVariable = []
        for label in inputsVariabName:
             selectedVariable.append(labels.index(label))
        inputs = [[float(data[i][j]) for j in selectedVariable] for i in range(len(data))]

        selectedOutput= []
        for label in outputsVariabName:
           selectedOutput.append(labels.index(label))
        outputs = [[float(data[i][j]) for j in selectedOutput] for i in range(len(data))]

        return inputs, outputs
