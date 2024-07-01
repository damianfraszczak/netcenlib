import networkx as nx
from networkx import Graph

from netcenlib.constants import INFINITY


def eccentricity_centrality(network: Graph) -> dict[str, float]:
    """
    Compute the Eccentricity Centrality for each node in the graph G.

    Ref: https://networkx.org/documentation/stable/reference/algorithms/generated/networkx.algorithms.distance_measures.eccentricity.html
    It is a "smart" version of the eccentricity centrality, which handles edge cases smartly.

    :param network: NetworkX graph
    :return: Dictionary of nodes with computed centrality as the value
    """

    if nx.number_connected_components(network) > 1:
        return {v: -INFINITY for v in network.nodes()}
    if len(network) == 1:
        return {network.nodes[0]: 1}
    return nx.eccentricity(network)
