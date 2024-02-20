import networkx as nx
import numpy as np
from networkx import Graph


def hubbell_centrality(
    network: Graph, weight: str = "weight", weight_factor: float = 0.5
) -> dict[str, float]:
    """
    Compute the Hubbell Centrality for each node in the graph G.
    Ref: https://www.centiserver.org/?q1=centrality&q2=Hubbell_Index

    :param network: NetworkX graph
    :param weight (str, optional): The edge attribute that holds the numerical value
        used as a weight. By default, it is 'weight'.
    :param weight_factor (float, optional): A scaling factor applied to the weights of
        the edges, representing the strength of interactions between nodes.
        It must be greater than 0 and less than 1 to ensure the matrix inversion
        needed for calculating Hubbell centrality is possible. The default value
        is 0.5, indicating moderate interaction strength.
    :return: Dictionary of nodes with computed centrality as the value
    """
    if not nx.is_weakly_connected(network):
        raise ValueError(
            "Hubbell centrality can only be computed for connected graphs."
        )

    weighted_adj_matrix = nx.to_numpy_array(network, weight=weight) * weight_factor

    if np.any(np.linalg.eigvals(weighted_adj_matrix) > 1):
        raise ValueError("Hubbell centrality is not solvable for this graph.")

    identity_matrix = np.eye(network.number_of_nodes())
    vector_e = np.ones((network.number_of_nodes(), 1))
    centrality_scores = np.linalg.solve(identity_matrix - weighted_adj_matrix, vector_e)

    return {
        node: score for node, score in zip(network.nodes(), centrality_scores.flatten())
    }
