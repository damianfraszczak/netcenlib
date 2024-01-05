from typing import List

from networkx import Graph


def exclude_nodes(G: Graph, nodes: List[any]) -> Graph:
    """
    Remove nodes from a graph.
    """
    g_copy = G.copy()
    g_copy.remove_nodes_from(nodes)
    return g_copy
