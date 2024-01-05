import networkx as nx
from collections import defaultdict


def bridgeness_centrality(network: nx.Graph) -> dict:
    """
    Compute the Bridgeness Centrality for each node in the graph G.
    Ref: https://www.centiserver.org/centrality/Bridgeness_Centrality/

    :param network: NetworkX graph
    :return: Dictionary of nodes with computed centrality as the value
    """
    bridges = list(nx.bridges(network))

    # Count the number of bridges each node is part of
    bridge_count = defaultdict(int)
    for u, v in bridges:
        bridge_count[u] += 1
        bridge_count[v] += 1

    # Normalize the bridge count by the maximum possible count
    max_bridge_count = max(bridge_count.values()) if bridge_count else 1
    bridgeness_cent = {node: bridge_count[node] / max_bridge_count for node in network.nodes()}

    return bridgeness_cent
