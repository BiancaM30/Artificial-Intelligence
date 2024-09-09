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
            chr.fitness = self.__params['fitness'](chr.repres, self.__graph)

    def best_chromosome(self):
        best = self.__population[0]
        for chromosome in self.__population:
            if (chromosome.fitness > best.fitness):
                best = chromosome
        return best

    def worst_chromosome(self):
        worst = self.__population[0]
        for chromosome in self.__population:
            if (chromosome.fitness < worst.fitness):
                worst = chromosome
        return worst

    def selection(self):
        pos1 = randint(0, self.__params['population_size'] - 1)
        pos2 = randint(0, self.__params['population_size'] - 1)
        if self.__population[pos1].fitness > self.__population[pos2].fitness:
            return pos1
        else:
            return pos2

    def one_generation_elitism(self):
        new_population = [self.best_chromosome()]
        for _ in range(self.__params['population_size'] - 1):
            p1 = self.__population[self.selection()]
            p2 = self.__population[self.selection()]
            offspring = p1.crossover(p2)
            offspring.mutation()
            new_population.append(offspring)
        self.__population = new_population
        self.evaluation()

