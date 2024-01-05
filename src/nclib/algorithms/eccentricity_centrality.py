import networkx as nx
from networkx import Graph


def eccentricity_centrality(network: Graph) -> dict[str, float]:
    """
    Compute the Eccentricity Centrality for each node in the graph G.
    Ref: https://www.centiserver.org/centrality/Eccentricity_Centrality/

    :param network: NetworkX graph
    :return: Dictionary of nodes with computed centrality as the value
    """
    eccentricity = nx.eccentricity(network)

    eccentricity_centrality = {node: 1.0 / ecc for node, ecc in
                               eccentricity.items()}

    return eccentricity_centrality
