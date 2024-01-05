import networkx as nx
from networkx import Graph


def centroid_centrality(network: Graph) -> dict[str, int]:
    """
    Compute the Centroid Centrality for each node in the graph G.
    Ref: https://www.centiserver.org/centrality/Centroid_value/

    :param network: NetworkX graph
    :return: Dictionary of nodes with computed centrality as the value
    """
    centroid_val = {}
    for node in network.nodes():
        shortest_paths = nx.shortest_path_length(network, source=node)
        avg_path_length = sum(shortest_paths.values()) / len(network.nodes())
        centroid_val[node] = sum(1 for _, length in shortest_paths.items() if length > avg_path_length)

    return centroid_val
