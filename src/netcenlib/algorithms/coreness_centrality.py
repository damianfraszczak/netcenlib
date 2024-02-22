import networkx as nx
from networkx import Graph


def coreness_centrality(network: Graph) -> dict[str, int]:
    """
    Compute the Coreness Centrality for each node in the graph G.

    Ref: https://www.centiserver.org/centrality/Coreness_Centrality/

    :param network: NetworkX graph
    :return: Dictionary of nodes with computed centrality as the value
    """
    core_numbers = nx.core_number(network)

    centrality = {
        node: sum([core_numbers[n] for n in network.neighbors(node) or [0]])
        / network.degree(node)
        for node in network.nodes()
    }

    return centrality
