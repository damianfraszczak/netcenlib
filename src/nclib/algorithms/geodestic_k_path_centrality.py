import networkx as nx

from nclib.common import nx_cached


def geodestic_k_path_centrality(network: nx.Graph, k: int = 3) -> dict[str, float]:
    """
    Compute the Geodesic K-Path Centrality for each node in the graph G.
    Ref: https://www.centiserver.org/centrality/Geodesic_K-Path_Centrality/

    :param network: NetworkX graph
    :param k: number of paths
    :return: Dictionary of nodes with computed centrality as the value
    """
    centrality = {}

    if k <= 0:
        raise ValueError("The k parameter must be greater than 0.")

    for v in network.nodes():
        sp = nx_cached.single_source_shortest_path_length(network, v)
        centrality[v] = sum(
            1 for dist in sp.values() if dist <= k and dist != 0)

    return centrality
