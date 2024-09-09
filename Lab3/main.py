import matplotlib.pyplot as plot
import networkx as nx
import numpy as np

from ga import GA
from graph import Graph

from utils import modularity, node_communities, get_communities_composition, cscore


def main():
    graph = Graph("input/karate.gml")
    graph.read_file()

    print("nr of nodes: ", graph.nodes)
    print("nr_of_edges", graph.edges)

    params = {'population_size': 30,
              'generations_number': 50,
              'fitness': modularity,
              'min': 0,
              'max': graph.nodes,
              'size': graph.nodes
              }

    ga = GA(params, graph)
    ga.initialisation()
    ga.evaluation()
    print("Population:", ga.population)

    all_best_fitnesses = []
    best_community_no = []
    best_chromosome = ga.best_chromosome()

    for generation in range(params['generations_number'] + 1):
        ga.one_generation_elitism()
        best_chromosome = ga.best_chromosome()
        communities = node_communities(best_chromosome.repres)
        best_community_no.append(max(communities))

        print('Best solution in generation ' + str(generation) +
              ' has: ' + str(best_community_no[-1]) + ' communities' +
              ', has a fitness: f(x) = ' + str(best_chromosome.fitness) +
              ', best chromosome is: x = ' + str(best_chromosome.repres))

        all_best_fitnesses.append(best_chromosome.fitness)

    print("\nAll fitnesses of generations:")
    print(all_best_fitnesses)

    print("\nNumber of communities per generation:")
    print(best_community_no)

    communities = node_communities(best_chromosome.repres)  # communities[i] represents community number of node i
    print('\nBelonging to a certain community for each node of the final network')
    print(communities)

    print("\nCommunities of final generation:")
    for comm in get_communities_composition(communities).values():
        print(comm)


    #plot network
    plot.ylabel('Fitness')
    plot.plot(all_best_fitnesses)
    plot.xlabel('Generation')
    plot.show()

    color = best_chromosome.repres
    matrix = np.matrix(graph.adj_matrix)
    G = nx.from_numpy_matrix(matrix)
    pos = nx.spring_layout(G)
    plot.figure(figsize=(4, 4))
    nx.draw_networkx_nodes(G, pos, node_size=50, cmap=plot.cm.RdYlBu, node_color=communities)
    nx.draw_networkx_edges(G, pos, alpha=0.3)
    plot.show()



main()
