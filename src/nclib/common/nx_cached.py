from typing import Any

import networkx as nx
from networkx import Graph


def cached_all_shortest_paths(network: Graph, source: Any, target: Any):
    return nx.all_shortest_paths(network, source=source, target=target)
