import networkx as nx
from networkx import Graph


def barycenter_centrality(network: Graph) -> dict[str, float]:
    """
    Compute the Barycenter Centrality for each node in the graph G.
    Ref: https://www.centiserver.org/centrality/Barycenter_Centrality/

    :param network: NetworkX graph
    :return: Dictionary of nodes with computed centrality as the value
    """
    centrality = {}

    for node in network.nodes():
        sp = dict(nx.shortest_path_length(network, source=node))
        centrality[node] = 1 / sum(sp) if sp else 0

    return centrality
