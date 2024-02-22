import networkx as nx

from netcenlib.common import nx_cached, nx_utils


def pdi_centrality(network: nx.Graph) -> dict[str, float]:
    """
    Compute the Pairwise Disconnectivity Index for each node in the graph G.

    Ref: https://www.centiserver.org/centrality/Pairwise_Disconnectivity_Index/

    :param network: NetworkX graph
    :return: Dictionary of nodes with computed centrality as the value
    """
    centrality = {}

    if not network.is_directed():
        raise ValueError("Graph must be directed")

    all_sp = dict(nx_cached.all_pairs_shortest_path_length(network))
    all_paths = sum(len(paths) for paths in all_sp.values()) - len(network.nodes())

    for node in network.nodes():
        g = nx_utils.exclude_nodes(network, [node])
        sp = dict(nx_cached.all_pairs_shortest_path_length(g))
        paths = sum(len(paths) for paths in sp.values()) - len(g.nodes())
        centrality[node] = (all_paths - paths) / all_paths if all_paths != 0 else 0

    return centrality
