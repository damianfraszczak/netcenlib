import networkx as nx
import numpy as np
from networkx import Graph

from nclib.common import nx_cached
from nclib.constants import INFINITY


def centroid_centrality(network: Graph) -> dict[str, int]:
    """
    Compute the Centroid Centrality for each node in the graph G.
    Ref: https://www.centiserver.org/centrality/Centroid_value/

    :param network: NetworkX graph
    :return: Dictionary of nodes with computed centrality as the value
    """
    centrality = {}

    N = network.number_of_nodes()
    gamma_values = np.zeros((N, N))
    nodes = list(network.nodes())

    for node in nodes:
        for v in nodes:
            for w in nodes:
                length_node_w = nx_cached.shortest_path_length(network,
                                                               source=node,
                                                               target=w)
                length_v_w = nx_cached.shortest_path_length(
                    network, source=v, target=w)
                if length_node_w < length_v_w:
                    gamma_values[node, v] += 1

    f_values = np.zeros((N, N))

    for node in nodes:
        for v in nodes:
            f_values[node, v] = gamma_values[node, v] - gamma_values[v, node]

    for node in nodes:
        result = INFINITY
        for i in nodes:
            if f_values[node, i] < result and node != i:
                result = f_values[node, i]
        centrality[node] = result

    return centrality
