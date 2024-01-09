from functools import cache, lru_cache
from typing import Any

import networkx as nx
from networkx import Graph

MAX_SIZE = 64


@lru_cache(maxsize=MAX_SIZE)
def all_shortest_paths(network: Graph, source: Any, target: Any):
    return nx.all_shortest_paths(network, source=source, target=target)


@lru_cache(maxsize=MAX_SIZE)
def single_source_shortest_path_length(network: Graph, v: Any):
    return nx.single_source_shortest_path_length(network, v)


@lru_cache(maxsize=MAX_SIZE)
def all_pairs_shortest_path_length(network: Graph):
    return nx.all_pairs_shortest_path_length(network)


@lru_cache(maxsize=MAX_SIZE)
def shortest_path_length(network: Graph, source: Any, target: Any):
    return nx.shortest_path_length(network, source=source, target=target)
