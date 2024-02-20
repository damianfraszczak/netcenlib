import networkx as nx
from networkx import Graph

from netcenlib.common import nx_cached
from netcenlib.constants import INFINITY


def radiality_centrality(network: Graph) -> dict[str, float]:
    """
    Compute the Radiality Centrality for each node in the graph G.
    Ref: https://www.centiserver.org/centrality/Radiality_Centrality/

    :param network: NetworkX graph
    :return: Dictionary of nodes with computed centrality as the value
    """
    centrality = {}

    N = network.number_of_nodes()
    diam = nx.diameter(network)

    for node in network.nodes():
        sp = nx_cached.single_source_shortest_path_length(network, node)
        rad = 0.0

        for v in network.nodes():
            if v in sp:
                rad += diam + 1.0 - sp[v]
            else:
                rad = INFINITY
                break

        centrality[node] = rad / (N - 1.0) if rad != INFINITY else INFINITY

    return centrality
