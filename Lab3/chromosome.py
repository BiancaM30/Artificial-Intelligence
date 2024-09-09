from random import randint

import numpy as np

from utils import generate_random_neighbour_of_node


class Chromosome:
    def __init__(self, params, graph):
        self.__params = params
        self.__graph = graph
        self.__fitness = 0.0

        self.__repres = np.zeros(self.__graph.nodes, dtype=int)
        for i in range(self.__graph.nodes):
            self.__repres[i] = generate_random_neighbour_of_node(i, self.__graph)

    @property
    def repres(self):
        return self.__repres

    @property
    def fitness(self):
        return self.__fitness

    @repres.setter
    def repres(self, l=[]):
        self.__repres = l

    @fitness.setter
    def fitness(self, fit=0.0):
        self.__fitness = fit

    # standard uniform crossover
    def crossover(self, second):
        mask = np.zeros(self.__params['size'], dtype=int)
        for i in range(self.__params['size']):
            mask[i] = randint(0, 1)

        offspring = Chromosome(self.__params, self.__graph)
        off_aux= []
        for i in range(self.__params['size']):
            if mask[i] == 1:
                off_aux.append(self.repres[i])
            else:
                off_aux.append(second.repres[i])

        offspring.repres = off_aux
        return offspring

    def mutation(self):
        pos = randint(0, len(self.repres) - 1)
        self.repres[pos] = generate_random_neighbour_of_node(pos, self.__graph)

    def __str__(self):
        return '\nChromosome: ' + str(self.__represres) + ' has a fitness of: ' + str(self.__fitness)

    def __repres__(self):
        return self.__str__()

    def __eq__(self, c):
        return self.__represres == c.__represres and self.__fitness == c.__fitness
