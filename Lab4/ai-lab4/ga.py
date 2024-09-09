from random import randint

from chromosome import Chromosome


class GA:
    def __init__(self, params, graph):
        self.__params = params
        self.__graph = graph
        self.__population = []

    @property
    def population(self):
        return self.__population

    def initialisation(self):
        for i in range(self.__params['population_size']):
            chr = Chromosome(self.__params, self.__graph)
            self.__population.append(chr)

    def evaluation(self):
        for chr in self.__population:
            chr.fitness = self.__params['fitness'](chr.repres, self.__graph.matrix)

    def best_chromosome(self):
        best = self.__population[0]
        for chromosome in self.__population:
            if (chromosome.fitness < best.fitness):
                best = chromosome
        return best

    def worst_chromosome(self):
        worst = self.__population[0]
        for chromosome in self.__population:
            if (chromosome.fitness > worst.fitness):
                worst = chromosome
        return worst

    def selection(self):
        pos1 = randint(0, self.__params['population_size'] - 1)
        pos2 = randint(0, self.__params['population_size'] - 1)
        if self.__population[pos1].fitness < self.__population[pos2].fitness:
            return pos1
        else:
            return pos2

    def next_generation_steady_state(self):
        for _ in range(self.__params['population_size']):
            p1 = self.__population[self.selection()]
            p2 = self.__population[self.selection()]
            off = p1.crossover(p2)

            off.mutation(self.__params['prob'])
            off.fitness = self.__params['fitness'](off.repres, self.__graph.matrix)
            worst = self.worst_chromosome()
            if off.fitness < worst.fitness:
                for i in range(self.__params['population_size']):
                    if self.population[i] == worst:
                        self.population[i] = off
                        break
