import networkx as nx
import numpy as np
from networkx import Graph


def heatmap_centrality(network: Graph) -> dict[str, float]:
    """
    Compute the Heatmap Centrality for each node in the graph G.

    Ref: https://www.centiserver.org/centrality/Heatmap_Centrality/

    :param network: NetworkX graph
    :return: Dictionary of nodes with computed centrality as the value
    """
    closeness_centrality = nx.closeness_centrality(network)
    # 1. Calculate the farness of each node in G
    node_farness = np.array(
        [
            1 / closeness_centrality[node] if closeness_centrality[node] != 0 else 0
            for node in network.nodes()
        ]
    )
    # 2. Calculate the sum of the farness of the neighbors for each node in G
    A = nx.to_numpy_array(network)
    neighbor_farness = A.dot(node_farness)
    # 3. Calculate the average sum of the farness of the neighbors for each node in G
    degrees = np.array([network.degree(node) for node in network.nodes()])
    average_neighbor_farness = neighbor_farness / degrees
    # 4. Calculate the Heatmap Centrality of each node in G
    centrality = node_farness - average_neighbor_farness
    return dict(zip(network.nodes(), centrality))
