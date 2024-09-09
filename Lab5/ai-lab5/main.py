import sys

from matplotlib import pyplot as plt

from ant import Ant
from colony import Colony
from graph import Graph
import numpy as np
import matplotlib

def main():
    graph = Graph("data/djibouti.tsp")
    graph.read_tsp_file()

    params = {'colonySize': 20, 'iterationsNumber': 50,
              'alpha': 3, 'beta': 6, 'ro': 0.1,
              'initPheromone': 0.2, 'q0': 0.5}

    colony = Colony(graph, params)

    global_best_ant = Ant(graph.nodes)
    global_best_ant.distance = sys.maxsize

    for i in range(params['iterationsNumber']):
        colony.solve()
        best_ant = colony.best_solution()
        print("Best solution in generation " + str(i) + ": " + str(best_ant.visited) +
              " has a cost cost of: " + str(best_ant.distance))
        colony.update_best_ant_pheromone(best_ant)
        if best_ant.distance < global_best_ant.distance:
            global_best_ant = best_ant
        #colony.dynamic()

    print("\nBest ant: " + str(global_best_ant.visited) + ", has a cost of: " + str(global_best_ant.distance))




main()
