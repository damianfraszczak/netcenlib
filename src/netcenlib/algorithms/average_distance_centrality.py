import networkx as nx
from networkx import Graph


def average_distance_centrality(network: Graph) -> dict[str, float]:
    """
    Compute the Average Distance Centrality for each node in the graph G.
    Ref: https://www.centiserver.org/centrality/Average_Distance/

    :param network: NetworkX graph
    :return: Dictionary of nodes with computed centrality as the value
    """

    centrality = {}
    n = network.number_of_nodes() + 1

    for v in network.nodes():
        sp = dict(nx.shortest_path_length(network, source=v))
        centrality[v] = sum(sp.values()) / n

    return centrality
