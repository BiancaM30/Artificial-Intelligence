# The evaluation function takes a path in the population.
# It gets the distance between each node pair in the path, by
# calling a function to read from the distance array. Adds them
# together and returns the sum as the cost of the path

def fitness(chromosome, matrix):
    cost_path = 0
    for i in range(len(chromosome) - 1):
        cost_path += matrix[chromosome[i] - 1][chromosome[i + 1] - 1]
    return cost_path