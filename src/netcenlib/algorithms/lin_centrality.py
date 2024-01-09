import networkx as nx

from netcenlib.common import nx_cached


def lin_centrality(network: nx.Graph) -> dict[str, float]:
    """
    Compute the Lin Centrality for each node in the graph G.
    Ref: https://www.centiserver.org/centrality/Lin_Centrality/

    :param network: NetworkX graph
    :return: Dictionary of nodes with computed centrality as the value
    """
    centrality = {}

    for node in network.nodes():
        sp = nx_cached.single_source_shortest_path_length(network, node)
        linrow = [sp[target] for target in sp if target != node]
        centrality[node] = ((len(linrow)) ** 2) / sum(linrow) if linrow else 0

    return centrality
