import pytest
from networkx import Graph

from netcenlib import Centrality, compute_centrality
from netcenlib.algorithms import (
    algebraic_centrality,
    average_distance_centrality,
    barycenter_centrality,
    betweenness_centrality,
    bottle_neck_centrality,
    centroid_centrality,
    closeness_centrality,
    cluster_rank_centrality,
    communicability_betweenness_centrality,
    coreness_centrality,
    current_flow_betweenness_centrality,
    current_flow_closeness_centrality,
    decay_centrality,
    degree_centrality,
    diffusion_degree_centrality,
    eccentricity_centrality,
    eigenvector_centrality,
    entropy_centrality,
    geodestic_k_path_centrality,
    group_betweenness_centrality,
    group_closeness_centrality,
    group_degree_centrality,
    harmonic_centrality,
    heatmap_centrality,
    hubbell_centrality,
    katz_centrality,
    laplacian_centrality,
    leverage_centrality,
    lin_centrality,
    mnc_centrality,
    pdi_centrality,
    percolation_centrality,
    radiality_centrality,
    rumor_centrality,
    second_order_centrality,
    semi_local_centrality,
    subgraph_centrality,
    topological_centrality,
)

CENTRALITY_MAPPING = {
    Centrality.ALGEBRAIC: algebraic_centrality.__name__,
    Centrality.AVERAGE_DISTANCE: average_distance_centrality.__name__,
    Centrality.BARYCENTER: barycenter_centrality.__name__,
    Centrality.BETWEENNESS: betweenness_centrality.__name__,
    Centrality.BOTTLE_NECK: bottle_neck_centrality.__name__,
    Centrality.CENTROID: centroid_centrality.__name__,
    Centrality.CLOSENESS: closeness_centrality.__name__,
    Centrality.CLUSTER_RANK: cluster_rank_centrality.__name__,
    Centrality.COMMUNICABILITY_BETWEENNESS: communicability_betweenness_centrality.__name__,
    Centrality.CORENESS: coreness_centrality.__name__,
    Centrality.CURRENT_FLOW_BETWEENNESS: current_flow_betweenness_centrality.__name__,
    Centrality.CURRENT_FLOW_CLOSENESS: current_flow_closeness_centrality.__name__,
    Centrality.DECAY: decay_centrality.__name__,
    Centrality.DEGREE: degree_centrality.__name__,
    Centrality.DIFFUSION_DEGREE: diffusion_degree_centrality.__name__,
    Centrality.ECCENTRICITY: eccentricity_centrality.__name__,
    Centrality.EIGENVECTOR: eigenvector_centrality.__name__,
    Centrality.ENTROPY: entropy_centrality.__name__,
    Centrality.GEODESTIC_K_PATH: geodestic_k_path_centrality.__name__,
    Centrality.GROUP_BETWEENNESS: group_betweenness_centrality.__name__,
    Centrality.GROUP_CLOSENESS: group_closeness_centrality.__name__,
    Centrality.GROUP_DEGREE: group_degree_centrality.__name__,
    Centrality.HARMONIC: harmonic_centrality.__name__,
    Centrality.HUBBELL: hubbell_centrality.__name__,
    Centrality.HEATMAP: heatmap_centrality.__name__,
    Centrality.KATZ: katz_centrality.__name__,
    Centrality.LAPLACIAN: laplacian_centrality.__name__,
    Centrality.LEVERAGE: leverage_centrality.__name__,
    Centrality.LIN: lin_centrality.__name__,
    Centrality.LOAD: "load_centrality",  # imported with different name
    Centrality.MNC: mnc_centrality.__name__,
    Centrality.PAGERANK: "pagerank_centrality",  # imported with different name
    Centrality.PDI: pdi_centrality.__name__,
    Centrality.PERCOLATION: percolation_centrality.__name__,
    Centrality.RADIALITY: radiality_centrality.__name__,
    Centrality.RUMOR: rumor_centrality.__name__,
    Centrality.SECOND_ORDER: second_order_centrality.__name__,
    Centrality.SEMI_LOCAL: semi_local_centrality.__name__,
    Centrality.SUBGRAPH: subgraph_centrality.__name__,
    Centrality.TOPOLOGICAL: topological_centrality.__name__,
    Centrality.TROPHIC_LEVELS: "trophic_levels_centrality",  # imported with different name
}


@pytest.fixture
def mock_compute_centrality(mocker):
    """Mock the compute_centrality function."""
    return mocker.patch(
        "netcenlib.centrality.compute_centrality", return_value="mocked_result"
    )


@pytest.fixture
def example_graph():
    """Return an example graph."""
    return Graph()


def test_compute_centrality(mocker):
    """Ensure correct mapping between Centrality enum and functions."""
    for centrality in Centrality:
        graph = Graph()
        mock = mocker.patch(
            f"netcenlib.algorithms.{CENTRALITY_MAPPING[centrality]}",
            return_value="mocked_result",
        )

        compute_centrality(graph, centrality)

        mock.assert_called_once_with(graph), f"Failed assert for {centrality}"
