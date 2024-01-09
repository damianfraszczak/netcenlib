import networkx as nx
import numpy as np

from netcenlib.common import nx_utils


def entropy_centrality(network: nx.Graph) -> dict[str, float]:
    """
    Compute the Entropy Centrality for each node in the graph G.
    Ref: https://www.centiserver.org/centrality/Entropy_Centrality/

    :param network: NetworkX graph
    :return: Dictionary of nodes with computed centrality as the value
    """
    centrality = {}

    for v in network.nodes():
        g = nx_utils.exclude_nodes(network, [v])
        sp = dict(nx.shortest_path_length(g))

        paths = sum(len(paths_dict) - 1 for paths_dict in sp.values()) / 2

        H = 0.0

        if paths > 0:
            for vv in g.nodes():
                Y = (len(sp[vv]) - 1) / paths
                if Y > 0:
                    H += Y * np.log2(Y)

        centrality[v] = -H

    return centrality
