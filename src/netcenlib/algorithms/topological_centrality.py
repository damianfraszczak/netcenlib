import networkx as nx
from networkx import Graph


def topological_centrality(network: Graph) -> dict[str, float]:
    """
    Compute the Topological Centrality for each node in the graph G.
    Ref: https://www.centiserver.org/centrality/Topological_Coefficient/

    :param network: NetworkX graph
    :return: Dictionary of nodes with computed centrality as the value
    """
    centrality = {}

    if nx.is_directed(network):
        raise ValueError("Graph must be undirected")

    for node in network.nodes():
        node_neighbors = set(nx.neighbors(network, node))
        shared_nodes = set()
        tc = 0
        for v in node_neighbors:
            v_neighbors = set(nx.neighbors(network, v)) - {node}
            for n in v_neighbors:
                tc += 1
                if n not in shared_nodes:
                    shared_nodes.add(n)
                    if n in node_neighbors:
                        tc += 1

        centrality[node] = (
            tc / (len(shared_nodes) * len(node_neighbors))
            if shared_nodes and node_neighbors
            else 0
        )

    return centrality
