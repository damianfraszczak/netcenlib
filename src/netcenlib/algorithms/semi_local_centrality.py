import networkx as nx
from networkx import Graph


def semi_local_centrality(network: Graph) -> dict[str, float]:
    """
    Compute the Semi Local Centrality for each node in the graph G.

    Ref: https://www.centiserver.org/centrality/Semi_Local_Centrality/

    :param network: NetworkX graph
    :return: Dictionary of nodes with computed centrality as the value
    """
    centrality = {}

    for node in network.nodes():
        node_neighbors = set(nx.neighbors(network, node))
        sl = 0
        for v in node_neighbors:
            v_neighbors = set(nx.neighbors(network, v))
            for vv in v_neighbors:
                vv_two_step_neighbors = set(
                    nx.single_source_shortest_path_length(network, vv, cutoff=2).keys()
                ) - {vv}
                sl += len(vv_two_step_neighbors)

        centrality[node] = sl

    return centrality
