from math import sqrt

class Graph:
    def __init__(self, filename):
        self.__filename = filename
        self.__nodes = 0
        self.__matrix = []

    @property
    def nodes(self):
        return self.__nodes

    @property
    def matrix(self):
        return self.__matrix

    def read_tsp_file(self):
        f = open(self.__filename, "r")
        line = f.readline()
        while not line[0].isnumeric():
            line = f.readline()
        coords = line.split(" ")
        coordinates_list = [[float(coords[1]), float(coords[2])]]
        line = f.readline()
        while line[0].isnumeric():
            coords = line.split(" ")
            coordinates_list.append([float(coords[1]), float(coords[2])])
            line = f.readline()
        self.__nodes = len(coordinates_list)
        distance_matrix = []
        for i in range(self.__nodes):
            distances_line = [0 for _ in range(self.__nodes)]
            for j in range(self.__nodes):
                if i != j:
                    distance_between_nodes = sqrt((coordinates_list[i][0] - coordinates_list[j][0]) ** 2 + (coordinates_list[i][1] - coordinates_list[j][1]) ** 2)
                    distances_line[j] = distance_between_nodes
            distance_matrix.append(distances_line)
        self.__matrix = distance_matrix
        f.close()

