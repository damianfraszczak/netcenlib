import networkx as nx
from networkx import Graph


def decay_centrality(network: Graph, decay_factor: float = 0.5) -> dict[str, float]:
    """
    Compute the Decay Centrality for each node in the graph G.
    Ref: https://www.centiserver.org/centrality/Decay_Centrality/

    :param network: NetworkX graph
    :return: Dictionary of nodes with computed centrality as the value
    """
    centrality = {}

    if decay_factor <= 0 or decay_factor >= 1:
        raise ValueError("The decay parameter must be between 0 and 1")


    for v in network.nodes():
        sp = nx.shortest_path_length(network, source=v)
        centrality[v] = sum(decay_factor ** length for target, length in sp.items() if
                            target != v)

    return centrality
