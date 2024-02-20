from typing import List

import networkx as nx
from networkx import Graph


def diffusion_degree_centrality(
    network: Graph, lambda_factor: [float, List[float]] = 1
) -> dict[str, float]:
    """
    Compute the Diffusion Degree Centrality for each node in the graph G.
    Ref: https://www.centiserver.org/centrality/Diffusion_Degree/

    :param network: NetworkX graph
    :param lambda_factor: Vector or numeric value providing propagation
    probability of nodes, default 1
    :return:  Dictionary of nodes with computed centrality as the value
    """
    centrality = {}

    degree_affected_by_lambda = {
        node: network.degree(node) * lambda_factor for node in network.nodes()
    }

    for v in network.nodes():
        neighbors = list(nx.neighbors(network, v))
        sm = sum(degree_affected_by_lambda[n] for n in neighbors)
        centrality[v] = sm + degree_affected_by_lambda[v]

    return centrality
