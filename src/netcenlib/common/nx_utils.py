import json
from typing import List

import networkx as nx
from networkx import Graph


def exclude_nodes(G: Graph, nodes: List[any]) -> Graph:
    """
    Remove nodes from a graph.
    """
    g_copy = G.copy()
    g_copy.remove_nodes_from(nodes)
    return g_copy

def load_network_json(json_file_path):
    with open(json_file_path, 'r') as f:
        data_loaded = json.load(f)
    return nx.node_link_graph(data_loaded)


def save_network_json(graph, json_file_path):
    data = nx.node_link_data(graph)
    with open(json_file_path, 'w') as f:
        json.dump(data, f, indent=4)
