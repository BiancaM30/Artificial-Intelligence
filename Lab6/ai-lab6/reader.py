import csv


class Reader:
    def __init__(self, file):
        self.file = file

    def read_regression(self, real, predicted):
        data_real = []
        data_predicted = []
        with open(self.file) as csv_file:
            csvreader = csv.reader(csv_file, delimiter=',')
            list_of_rows = list(csvreader)

        data_real = [[] for i in range(len(list_of_rows) - 1)]
        data_predicted = [[] for i in range(len(list_of_rows) - 1)]
        for i in range(1, len(list_of_rows)):
            data_real[i - 1].append(list_of_rows[i][0])
            data_real[i - 1].append(list_of_rows[i][1])
            data_real[i - 1].append(list_of_rows[i][2])
            data_predicted[i - 1].append(list_of_rows[i][3])
            data_predicted[i - 1].append(list_of_rows[i][4])
            data_predicted[i - 1].append(list_of_rows[i][5])

        real = [[float(data_real[i][j]) for j in range(3)] for i in range(len(data_real))]
        predicted = [[float(data_predicted[i][j]) for j in range(3)] for i in range(len(data_predicted))]

        return real, predicted

    def read_classification(self):
        real = []
        predicted = []
        with open(self.file) as csv_file:
            csvreader = csv.reader(csv_file, delimiter=',')
            list_of_rows = list(csvreader)

        for i in range(1, len(list_of_rows)):
            real.append(list_of_rows[i][0])
            predicted.append(list_of_rows[i][1])

        return real, predicted
