import networkx as nx


def mnc_centrality(network: nx.Graph) -> dict[str, float]:
    """
    Compute the MNC (Maximum Neighborhood Component) Centrality for each node in the graph G.
    Ref: https://www.centiserver.org/centrality/MNC_Maximum_Neighborhood_Component/

    :param network: NetworkX graph
    :return: Dictionary of nodes with computed centrality as the value
    """
    centrality = {}

    for node in network.nodes():
        neighbors = list(nx.neighbors(network, node))
        if neighbors:
            subgraph = network.subgraph(neighbors)
            components = nx.connected_components(subgraph)
            max_component_size = max(len(c) for c in components) if components else 0
            centrality[node] = max_component_size
        else:
            centrality[node] = 0

    return centrality
