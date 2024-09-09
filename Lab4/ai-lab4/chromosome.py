import random
import numpy as np


class Chromosome:
    def __init__(self, params, graph):
        self.__params = params
        self.__graph = graph
        self.__fitness = 0.0


        # get all nodes that are not source or destination
        middle = []
        for i in range(1, self.__params['size'] + 1):
            if i != self.__params['source_node'] and i != self.__params['source_dest']:
                middle.append(i)

        # generate permutation starting with node_source and ending with node_destination
        perm = [self.__params['source_node']]
        middle = np.random.permutation(middle)
        perm = perm + middle.tolist()
        perm.append(self.__params['source_dest'])

        self.__repres = perm

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

    def crossover(self, second):
        pos1 = random.randint(1, self.__params['size'] - 2)
        pos2 = random.randint(1, self.__params['size'] - 2)
        if pos2 < pos1:
            pos1, pos2 = pos2, pos1

        offspring = Chromosome(self.__params, self.__graph)
        k = 1
        newrepres = self.__repres[pos1:pos2]

        for node in second.repres[pos2:] + second.repres[:pos2]:
            if node not in newrepres and node!= self.__params['source_node']:
                if len(newrepres) < self.__params['size'] - pos1:
                    newrepres.append(node)
                else:
                    newrepres.insert(k, node)
                    k += 1
        newrepres.insert(0, self.__params['source_node'])
        newrepres.append(self.__repres[self.__params['size']])

        offspring.repres = newrepres
        return offspring


    def mutation(self, probability):
        for i in range(1, self.__params['size']):
            p = random.uniform(0, 1)
            if p < probability:
                pos = random.randint(2, self.__params['size'] - 2)
                self.__repres[i], self.__repres[pos] = self.__repres[pos], self.__repres[i]


    def __str__(self):
        return '\nChromosome: ' + str(self.__repres) + ' has a fitness of: ' + str(self.__fitness)


    def __repres__(self):
        return self.__str__()


    def __eq__(self, c):
        return self.__repres == c.__repres and self.__fitness == c.__fitness
