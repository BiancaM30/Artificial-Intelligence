from ga import GA
from graph import Graph

from utils import fitness


def main():
    graph = Graph("input/hard2.txt")
    graph.read_txt_file()

    params = {'population_size': 30,
              'generations_number': 3000,
              'fitness': fitness,
              'prob': 0.5,
              'size': graph.nodes,
              'source_node': 1,
              'source_dest': 1
              }

    ga = GA(params, graph)
    ga.initialisation()
    ga.evaluation()

    all_best_fitnesses = []
    best_chromosome = ga.best_chromosome()
    all_best_chromosomes = [ga.best_chromosome()]
    for generation in range(params['generations_number']):
        ga.next_generation_steady_state()
        best_chromosome = ga.best_chromosome()

        print('Best solution in generation ' + str(generation) +
              ', has a fitness: f(x) = ' + str(best_chromosome.fitness) +
              ', best chromosome is: x = ' + str(best_chromosome.repres))

        all_best_chromosomes.append(best_chromosome)
        all_best_fitnesses.append(best_chromosome.fitness)

    print("\nAll fitnesses of generations:")
    print(all_best_fitnesses)

    print("\nBest solution is: ")
    print(all_best_chromosomes[len(all_best_chromosomes) - 1])

    print("\nAll solutions with the same fitness:")
    all_solutions = [best_chromosome]
    for chr in all_best_chromosomes:
        if chr.fitness == best_chromosome.fitness:
            ok=1
            for el in all_solutions:
                 if chr.repres == el.repres:
                     ok=0
                     break
            if ok==1:
                all_solutions.append(chr)
    for solution in all_solutions:
        print(solution.repres)


main()
