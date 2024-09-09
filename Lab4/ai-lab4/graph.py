from cmath import sqrt

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

    def read_txt_file(self):
        f = open(self.__filename, "r")
        self.__nodes = int(f.readline())
        for i in range(self.nodes):
            self.__matrix.append([])
            line = f.readline()
            elems = line.split(",")
            for j in range(self.nodes):
                self.__matrix[-1].append(int(elems[j]))
        f.close()
