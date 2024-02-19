import json
import math
import os

from netcenlib.centrality import compute_centrality
from netcenlib.common.nx_utils import load_network_json
from netcenlib.taxonomies import Centrality

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))

DIRECTED_ALGORITHMS = {
    Centrality.PDI,
    Centrality.TROPHIC_LEVELS,
}

ALGORITHM_NETWORK_TEST_CASES = {
    "karate": [
        Centrality.ALGEBRAIC,
        Centrality.AVERAGE_DISTANCE,
        Centrality.BARYCENTER,
        Centrality.BETWEENNESS,
        Centrality.BOTTLE_NECK,
        Centrality.CENTROID,
        Centrality.CLOSENESS,
        Centrality.CLUSTER_RANK,
        Centrality.COMMUNICABILITY_BETWEENNESS,
        Centrality.CORENESS,
        Centrality.CURRENT_FLOW_BETWEENNESS,
        Centrality.CURRENT_FLOW_CLOSENESS,
        Centrality.DECAY,
        Centrality.DEGREE,
        Centrality.DIFFUSION,
        Centrality.EIGENVECTOR,
        Centrality.ENTROPY,
        Centrality.GEODESTIC,
        Centrality.HARMONIC,
        Centrality.HEATMAP,
        Centrality.KATZ,
        Centrality.LAPLACIAN,
        Centrality.LEVERAGE,
        Centrality.LIN,
        Centrality.LOAD,
        Centrality.MNC,
        Centrality.PAGERANK,
        Centrality.PERCOLATION,
        Centrality.RADIALITY,
        Centrality.RUMOR,
        Centrality.SECOND_ORDER,
        Centrality.SEMI_LOCAL,
        Centrality.SUBGRAPH,
        Centrality.TOPOLOGICAL,
    ],
    "gn_100": [
        Centrality.ALGEBRAIC,
        Centrality.AVERAGE_DISTANCE,
        Centrality.BETWEENNESS,
        Centrality.CLOSENESS,
        Centrality.CORENESS,
        Centrality.DECAY,
        Centrality.DIFFUSION,
        Centrality.ENTROPY,
        Centrality.GEODESTIC,
        Centrality.HARMONIC,
        Centrality.HEATMAP,
        Centrality.KATZ,
        Centrality.LAPLACIAN,
        Centrality.LEVERAGE,
        Centrality.LIN,
        Centrality.LOAD,
        Centrality.PAGERANK,
        Centrality.PDI,
        Centrality.PERCOLATION,
        Centrality.RUMOR,
        Centrality.SEMI_LOCAL,
        Centrality.TROPHIC_LEVELS,
    ],
}


def _load_network(network_name):
    file_path = os.path.join(
        CURRENT_DIR, os.path.join("networks", f"{network_name}.json")
    )
    return load_network_json(file_path)


def _get_centrality_result(centrality, network_name):
    centrality_name = centrality.name.lower().replace("centrality.", "")
    file_path = os.path.join(
        CURRENT_DIR, "expected", network_name, f"{centrality_name}.json"
    )
    with open(file_path, "r") as file:
        return json.load(file)


def _convert_keys_to_strings(data):
    if isinstance(data, dict):
        return {
            str(key): _convert_keys_to_strings(value) for key, value in data.items()
        }
    elif isinstance(data, list):
        return [_convert_keys_to_strings(item) for item in data]
    else:
        return data


def _assert_dicts_with_precision(centrality, item1, item2, tol=0.0001):
    if isinstance(item1, dict) and isinstance(item2, dict):
        for key in item1:
            assert (
                key in item2
            ), f"{centrality} - key {key} not found in both dictionaries"
            _assert_dicts_with_precision(centrality, item1[key], item2[key], tol)
    elif isinstance(item1, (float, int)) and isinstance(item2, (float, int)):
        assert math.isclose(
            item1, item2, abs_tol=tol
        ), f"{centrality} - Value differs more than {tol}"
    else:
        assert item1 == item2, f"{centrality} - Value differs"


def _assert_centrality(centrality, network_name, G):
    expected = _get_centrality_result(centrality, network_name)
    result = compute_centrality(G, centrality)
    results_key_str = _convert_keys_to_strings(result)

    _assert_dicts_with_precision(centrality, results_key_str, expected)


def test_algorithms():
    """Ensure algorithms return expected results."""
    for network_name, algorithms in ALGORITHM_NETWORK_TEST_CASES.items():
        G = _load_network(network_name)
        for centrality in algorithms:
            _assert_centrality(centrality, network_name, G)
