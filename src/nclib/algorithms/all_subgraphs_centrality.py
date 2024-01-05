import networkx as nx
from itertools import combinations


def all_subgraphs_centrality(network: nx.Graph):
    """
    Compute the All-subgraphs Centrality for each node in the graph G.
    Ref:  https://www.centiserver.org/centrality/All-subgraphs_Centrality/

    :param network: NetworkX graph
    :return: Dictionary of nodes with Rumor Centrality as the value
    """

    centrality = {node: 0 for node in network.nodes()}

    all_nodes = list(network.nodes())

    for r in range(1, len(all_nodes) + 1):
        for sub_nodes in combinations(all_nodes, r):
            subgraph = network.subgraph(sub_nodes)
            for node in subgraph.nodes():
                centrality[node] += 1

    return centrality
