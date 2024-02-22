"""Centrality measures for networks."""

import netcenlib.algorithms as ncl_algorithms
from netcenlib import Centrality


def compute_centrality(network, centrality: Centrality, *args, **kwargs):
    """Compute centrality measure for a given network."""
    centrality_function_name = f"{centrality.value.lower()}_centrality"
    print(centrality_function_name)
    return getattr(ncl_algorithms, centrality_function_name)(network, *args, **kwargs)
