import networkx as nx
import numpy as np


class Graph:
    def __init__(self, filename):
        self.__filename = filename
        self.__nodes = 0
        self.__edges = 0
        self.__adj_matrix = []
        self.__degree_list = []

    @property
    def nodes(self):
        return self.__nodes

    @property
    def edges(self):
        return self.__edges

    @property
    def adj_matrix(self):
        return self.__adj_matrix

    @property
    def degree_list(self):
        return self.__degree_list

    def read_file(self):
        graph = nx.read_gml(self.__filename, label='id')
        self.__nodes = len(graph.nodes)
        self.__edges = len(graph.edges)

        self.__adj_matrix = np.zeros((self.__nodes, self.__nodes), dtype=int)

        for edge in graph.edges:
            self.__adj_matrix[edge[0] - 1][edge[1] - 1] = 1
            self.__adj_matrix[edge[1] - 1][edge[0] - 1] = 1

        for i in range(self.__nodes):
            if i in graph.adj:
                self.__degree_list.append(len(graph.adj[i]))
            else:
                self.__degree_list.append(0)
