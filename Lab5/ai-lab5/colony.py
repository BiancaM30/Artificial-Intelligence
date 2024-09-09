from random import uniform, randint

import numpy as np

from ant import Ant


class Colony:
    def __init__(self, graph, params):
        self.graph = graph
        self.params = params
        self.population = []
        self.pheromone_matrix = [[0.0 for _ in range(graph.nodes)] for _ in range(graph.nodes)]

    def solve(self):
        self.population = []
        for _ in range(self.params['colonySize']):
            a = Ant(self.graph.nodes)
            self.population.append(a)

        for i in range(1, self.graph.nodes):
            for k in range(self.params['colonySize']):
                neighbour = self.next_node(k)
                self.population[k].visited.append(neighbour)

                # local pheromone update
                ro = self.params['ro']
                pos1 = self.population[k].visited[-2]
                pos2 = self.population[k].visited[-1]
                self.pheromone_matrix[pos1 - 1][pos2 - 1] = (1.0 - ro) * self.pheromone_matrix[pos1 - 1][
                    pos2 - 1] + ro * self.params['initPheromone']
                self.pheromone_matrix[pos2 - 1][pos1 - 1] = (1.0 - ro) * self.pheromone_matrix[pos2 - 1][
                    pos1 - 1] + ro * self.params['initPheromone']

        # calculate total distance traveled by ants
        for i in range(self.params['colonySize']):
            self.population[i].distance = self.compute_distance(self.population[i])

    def get_unvisited_nodes(self, k):
        node = self.population[k].visited[-1]
        unvisited = []
        for i in range(self.graph.nodes):
            if self.graph.matrix[node - 1][i] != 0 and i + 1 not in self.population[k].visited:
                unvisited.append(i + 1)
        return unvisited

    def next_node(self, k):
        unvisited = self.get_unvisited_nodes(k)
        node = self.population[k].visited[-1]

        alpha = self.params['alpha']
        beta = self.params['beta']
        wheel_sum = 0.0
        for i in unvisited:
            gama = self.pheromone_matrix[i - 1][node - 1]
            d = self.graph.matrix[i - 1][node - 1]
            eta = 1 / d
            wheel_sum += (gama ** alpha) * (eta ** beta)

        random_number = uniform(0, wheel_sum)
        wheel_position = 0.0
        for i in unvisited:
            gama = self.pheromone_matrix[i - 1][node - 1]
            d = self.graph.matrix[i - 1][node - 1]
            eta = 1 / d
            wheel_position += (gama ** alpha) * (eta ** beta)
            if wheel_position > random_number:
                return i
        return unvisited[0]

    def compute_distance(self, ant):
        distance = 0
        for i in range(len(ant.visited) - 1):
            distance += self.graph.matrix[ant.visited[i] - 1][ant.visited[i + 1] - 1]
        distance += self.graph.matrix[ant.visited[-1] - 1][ant.visited[0] - 1]
        return distance

    def best_solution(self):
        min_cost = self.population[0].distance
        min_index = 0
        for i in range(1, self.params['colonySize']):
            if self.population[i].distance < min_cost:
                min_cost = self.population[i].distance
                min_index = i
        return self.population[min_index]

    def update_best_ant_pheromone(self, best_ant):
        ro = self.params['ro']
        L_best = best_ant.distance
        delta_best = 1/L_best
        for i in range(1,self.graph.nodes-1):
            k = self.population.index(best_ant)
            node1 = self.population[k].visited[i]
            node2 = self.population[k].visited[i + 1]
            self.pheromone_matrix[node1 - 1][node2 - 1] = (1.0 - ro) * self.pheromone_matrix[node1 - 1][
                node2 - 1] + ro * delta_best
            self.pheromone_matrix[node2 - 1][node1 - 1] = (1.0 - ro) * self.pheromone_matrix[node2 - 1][
                node1 - 1] + ro * delta_best

    def dynamic(self):
        new_weight = randint(1, 1000)
        i = 0
        j = 0
        while i == j:
            i = randint(0, self.graph.nodes - 1)
            j = randint(0, self.graph.nodes - 1)
        self.graph.matrix[i][j] = new_weight
        self.graph.matrix[j][i] = new_weight
        print("Updated edge [" + str(i) + "," + str(j) + "] weight to " + str(new_weight))
