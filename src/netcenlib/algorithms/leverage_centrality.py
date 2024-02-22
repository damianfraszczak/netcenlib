import networkx as nx


def leverage_centrality(network: nx.Graph) -> dict[str, float]:
    """
    Compute the Leverage Centrality for each node in the graph G.

    Ref: https://www.centiserver.org/centrality/Leverage_Centrality/

    :param network: NetworkX graph
    :return: Dictionary of nodes with computed centrality as the value
    """
    centrality = {}

    nodes_degree = dict(network.degree())

    for node in network.nodes():
        neighbors = list(nx.neighbors(network, node))
        node_centrality = 0
        if neighbors:
            leverage_scores = [
                (nodes_degree[node] - nodes_degree[nb])
                / (nodes_degree[node] + nodes_degree[nb])
                for nb in neighbors
            ]
            node_centrality = sum(leverage_scores) / len(leverage_scores)
        centrality[node] = node_centrality

    return centrality
