import networkx as nx
import numpy as np

def heatmap_centrality(network):
    """
    Compute the Heatmap Centrality for each node in the graph G.
    Ref: https://www.centiserver.org/centrality/Heatmap_Centrality/

    :param network: NetworkX graph
    :return: Dictionary of nodes with computed centrality as the value
    """
    closeness_centrality = nx.closeness_centrality(network)
    node_farness = {node: 1 / closeness_centrality[node] for node in network.nodes()}

    A = nx.adjacency_matrix(network).todense()
    farness_array = np.array(list(node_farness.values()))
    neighbor_farness = np.dot(A, farness_array)

    degrees = np.array([degree for _, degree in network.degree()])
    avg_neighbor_farness = neighbor_farness / degrees

    heatmap_values = np.array(list(node_farness.values())) - avg_neighbor_farness

    return dict(zip(network.nodes(), heatmap_values))
