from networkx import Graph

from netcenlib.common import nx_cached


def decay_centrality(network: Graph, decay_factor: float = 0.5) -> dict[str, float]:
    """
    Compute the Decay Centrality for each node in the graph G.

    Ref: https://www.centiserver.org/centrality/Decay_Centrality/

    :param network: NetworkX graph
    :param decay_factor: Decay factor, default 0.5
    :return: Dictionary of nodes with computed centrality as the value
    """
    centrality = {}

    if decay_factor <= 0 or decay_factor >= 1:
        raise ValueError("The decay parameter must be between 0 and 1")

    for node in network.nodes():
        sp = dict(nx_cached.single_source_shortest_path_length(network, node))
        decayed_distances = [decay_factor**d for d in sp.values()]
        centrality[node] = sum(decayed_distances)

    return centrality
