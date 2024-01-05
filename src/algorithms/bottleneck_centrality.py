import networkx as nx
import numpy as np
from networkx import Graph


def bottle_neck_centrality(graph: Graph) -> dict[str, float]:
    """
    Compute the BottleNeck Centrality for each node in the graph G.
    Ref: https://www.centiserver.org/centrality/BottleNeck/

    :param network: NetworkX graph
    :return: Dictionary of nodes with computed centrality as the value
    """
    res = np.zeros(graph.number_of_nodes())
    for v in graph.nodes():
        all_paths = {
            target: list(nx.all_shortest_paths(graph, source=v, target=target))
            for target in graph.nodes() if target != v}
        path_counts = {}
        for target, paths in all_paths.items():
            for path in paths:
                for node in path[1:]:
                    if node != v:
                        path_counts[node] = path_counts.get(node, 0) + 1

        for i in path_counts:
            if path_counts[i] > (len(path_counts) / 4):
                res[i] += 1

    return dict(zip(graph.nodes(), res))
