import matplotlib.pyplot as plot
import networkx as nx
import numpy as np
import collections

from random import choice

from networkx.algorithms.community import girvan_newman


def get_communities_composition(network):
    nodes_of_community = {}
    for i in range(0, len(network)):
        if network[i] in nodes_of_community:
            nodes_of_community[network[i]].append(i)
        else:
            nodes_of_community[network[i]] = [i]
    return nodes_of_community


def modularity(communities, graph):
    M = 2 * graph.edges
    Q = 0.0
    for i in range(graph.nodes):
        for j in range(graph.nodes):
            if communities[i] == communities[j]:
                Q += (graph.adj_matrix[i][j] - graph.degree_list[i] * graph.degree_list[j] / M)
    return Q * 1 / M

def column_sum(mat,i,noNodes):

    s = 0
    for j in range(0, noNodes):
        s = s + mat[i,j]

    return s

def cscore(communities, graph):

    C = max(node_communities(communities))
    noNodes = graph.nodes
    adj_matrix = graph.adj_matrix

    Q = 0.0
    alpha = 0.3
    sum = 0

    for i in range(0, C):
        Q += (pow(((1/C) * column_sum(adj_matrix,i,noNodes)),alpha)/C)

    for i in range(0, noNodes):
        for j in range(0, noNodes):
            sum = sum+adj_matrix[i,j]

    return Q*sum

def generate_random_neighbour_of_node(node, graph):
    node_row = graph.adj_matrix[node]
    neighbour_list = []
    for i in range(graph.nodes):
        if node_row[i] == 1:
            neighbour_list.append(i + 1)
    selected = choice(neighbour_list)
    return selected


def node_communities(network):
    def dfs(node):
        communities[node - 1] = no_of_communities
        visited.add(node)
        for n in dict_neighbour[node]:
            if n not in visited:
                dfs(n)

    edges = []
    dict_neighbour = collections.defaultdict(list)
    for i in range(len(network)):
        edges.append([i, network[i]])
        dict_neighbour[i].append(network[i])
        dict_neighbour[network[i]].append(i)

    visited = set()
    no_of_communities = 0
    communities = np.zeros(len(network), dtype=int)

    for i in range(1, len(network) + 1):
        if i not in visited:
            no_of_communities += 1
            dfs(i)
    return communities


