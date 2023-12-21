import networkx as nx
from networkx import Graph


def calculate_average_distance_centrality(network: Graph) -> dict:
    """
            Compute the Average Distance Centrality for each node in the graph G.
            Ref: https://www.centiserver.org/centrality/Average_Distance/

            :param network: NetworkX graph
            :return: Dictionary of nodes with computed centrality as the value
    """

    centrality = {}
    for node in network.nodes():
        path_lengths = nx.single_source_shortest_path_length(network, node)
        total_distance = sum(path_lengths.values())
        average_distance = total_distance / (len(network) - 1)
        centrality[node] = average_distance

    return centrality
