from decimal import Decimal
from random import shuffle
from typing import List

import networkx as nx
from networkx import Graph, DiGraph


def get_root(tree: DiGraph, node: int):
    return tree.in_edges(node)[0][0] if tree.in_edges(node) else None


def get_children(tree: DiGraph, node: int):
    return [out_edge[1] for out_edge in tree.out_edges([node])]


def get_leaves(tree: DiGraph):
    return [
        x for x in tree.nodes() if tree.out_degree(x) == 0 and tree.in_degree(x) == 1
    ]


def children_processed(tree: DiGraph, node: int, processed_nodes: List[int]) -> bool:
    children = get_children(tree, node)
    return len(children) == 0 or all(child in processed_nodes for child in children)


def rumor_centrality(network: Graph):
    """
        Compute the Rumor Centrality for each node in the graph G.
        Ref: https://www.centiserver.org/centrality/Rumor_Centrality/

        :param G: NetworkX graph
        :return: Dictionary of nodes with Rumor Centrality as the value
        """
    nodes = list(network)
    shuffle(nodes)
    N = len(nodes)
    rumorCentrality = {}

    for sourceNode in nodes:
        bfs_tree = nx.bfs_tree(network, sourceNode, False)
        messages_up = {}
        messages_down = {}
        leaves = get_leaves(bfs_tree)

        while not children_processed(
                bfs_tree, sourceNode, list(messages_down.keys())
        ):
            for node in nodes:
                if node in leaves:
                    messages_up[node] = 1
                    messages_down[node] = 1
                elif node != sourceNode:
                    if children_processed(
                            bfs_tree, node, list(messages_down.keys())
                    ):
                        node_children = get_children(bfs_tree, node)
                        msg_top = 0
                        msg_down = 1
                        for child in node_children:
                            msg_top = msg_top + messages_up[child]
                            msg_down = msg_down * messages_down[child]
                        messages_up[node] = msg_top + 1
                        messages_down[node] = messages_up[node] * msg_down

        source_children = get_children(bfs_tree, sourceNode)
        r = Decimal(1.0)
        for child in source_children:
            r = r / messages_down[child]
        r = r / N
        r = float(r)
        rumorCentrality[sourceNode] = r
    return rumorCentrality
