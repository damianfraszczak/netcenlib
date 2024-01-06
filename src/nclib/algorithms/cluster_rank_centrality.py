import networkx as nx
import numpy as np
from networkx import Graph

from nclib.constants import INFINITY


def cluster_rank_centrality(network: Graph) -> dict[str, int]:
    """
    Compute the ClusterRank Centrality for each node in the graph G.
    Ref: https://www.centiserver.org/centrality/ClusterRank/

    :param network: NetworkX graph
    :return: Dictionary of nodes with computed centrality as the value
    """
    centrality = {}

    if network.is_directed():
        cc = nx.clustering(network, nodes=None, weight=None, mode='dot')
        mode = "out"
    else:
        cc = nx.clustering(network, nodes=None, weight=None)
        mode = "all"

    for node in network.nodes():
        if np.isnan(cc[node]):
            centrality[node] = INFINITY
        else:
            if mode == "out":
                neighbors = set(network.successors(node))
            else:
                neighbors = set(nx.neighbors(network, node))

            cr = sum(
                network.degree(nb, weight=None) for nb in neighbors) + len(
                neighbors)
            centrality[node] = cr * cc[node]

    return centrality
