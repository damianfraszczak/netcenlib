import pytest
from networkx import (
    Graph,
    betweenness_centrality,
    closeness_centrality,
    communicability_betweenness_centrality,
    current_flow_betweenness_centrality,
    current_flow_closeness_centrality,
    degree_centrality,
    eigenvector_centrality,
    group_betweenness_centrality,
    group_closeness_centrality,
    group_degree_centrality,
    harmonic_centrality,
    katz_centrality,
    laplacian_centrality,
    load_centrality,
    pagerank,
    percolation_centrality,
    second_order_centrality,
    subgraph_centrality,
    trophic_levels,
)

from netcenlib.algorithms.algebraic_centrality import algebraic_centrality
from netcenlib.algorithms.average_distance_centrality import (
    average_distance_centrality,
)
from netcenlib.algorithms.barycenter_centrality import barycenter_centrality
from netcenlib.algorithms.bottle_neck_centrality import bottle_neck_centrality
from netcenlib.algorithms.centroid_centrality import centroid_centrality
from netcenlib.algorithms.cluster_rank_centrality import (
    cluster_rank_centrality,
)
from netcenlib.algorithms.coreness_centrality import coreness_centrality
from netcenlib.algorithms.decay_centrality import decay_centrality
from netcenlib.algorithms.diffusion_degree_centrality import (
    diffusion_degree_centrality,
)
from netcenlib.algorithms.entropy_centrality import entropy_centrality
from netcenlib.algorithms.geodestic_k_path_centrality import (
    geodestic_k_path_centrality,
)
from netcenlib.algorithms.heatmap_centrality import heatmap_centrality
from netcenlib.algorithms.leverage_centrality import leverage_centrality
from netcenlib.algorithms.lin_centrality import lin_centrality
from netcenlib.algorithms.mnc_centrality import mnc_centrality
from netcenlib.algorithms.pdi_centrality import pdi_centrality
from netcenlib.algorithms.radiality_centrality import radiality_centrality
from netcenlib.algorithms.rumor_centrality import rumor_centrality
from netcenlib.algorithms.semi_local_centrality import semi_local_centrality
from netcenlib.algorithms.topological_centrality import topological_centrality
from netcenlib.centrality import CENTRALITY_MAPPING, CentralityService
from netcenlib.taxonomies import Centrality


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


@pytest.fixture
def centrality_service(example_graph):
    """Return a CentralityService instance."""
    return CentralityService(example_graph)


@pytest.mark.parametrize("centrality_type", Centrality)
def test_centrality_methods(
    centrality_service, mock_compute_centrality, centrality_type
):
    """Ensure that the correct method is called for each centrality type."""
    method_name = centrality_type.name.lower()

    result = getattr(centrality_service, method_name)

    mock_compute_centrality.assert_called_with(
        centrality_service.network, centrality_type
    )
    assert result == "mocked_result"
    mock_compute_centrality.reset_mock()


def test_centrality_mapping():
    """Ensure correct mapping between Centrality enum and functions."""
    assert CENTRALITY_MAPPING[Centrality.ALGEBRAIC] == algebraic_centrality
    assert (
        CENTRALITY_MAPPING[Centrality.AVERAGE_DISTANCE] == average_distance_centrality
    )
    assert CENTRALITY_MAPPING[Centrality.BARYCENTER] == barycenter_centrality
    assert CENTRALITY_MAPPING[Centrality.BOTTLE_NECK] == bottle_neck_centrality
    assert CENTRALITY_MAPPING[Centrality.CENTROID] == centroid_centrality
    assert CENTRALITY_MAPPING[Centrality.CLUSTER_RANK] == cluster_rank_centrality
    assert CENTRALITY_MAPPING[Centrality.CORENESS] == coreness_centrality
    assert CENTRALITY_MAPPING[Centrality.DECAY] == decay_centrality
    assert CENTRALITY_MAPPING[Centrality.DIFFUSION] == diffusion_degree_centrality
    assert CENTRALITY_MAPPING[Centrality.ENTROPY] == entropy_centrality
    assert CENTRALITY_MAPPING[Centrality.GEODESTIC] == geodestic_k_path_centrality
    assert CENTRALITY_MAPPING[Centrality.HEATMAP] == heatmap_centrality
    assert CENTRALITY_MAPPING[Centrality.LEVERAGE] == leverage_centrality
    assert CENTRALITY_MAPPING[Centrality.LIN] == lin_centrality
    assert CENTRALITY_MAPPING[Centrality.MNC] == mnc_centrality
    assert CENTRALITY_MAPPING[Centrality.PDI] == pdi_centrality
    assert CENTRALITY_MAPPING[Centrality.RADIALITY] == radiality_centrality
    assert CENTRALITY_MAPPING[Centrality.RUMOR] == rumor_centrality
    assert CENTRALITY_MAPPING[Centrality.SEMI_LOCAL] == semi_local_centrality
    assert CENTRALITY_MAPPING[Centrality.TOPOLOGICAL] == topological_centrality
    assert CENTRALITY_MAPPING[Centrality.BETWEENNESS] == betweenness_centrality
    assert CENTRALITY_MAPPING[Centrality.CLOSENESS] == closeness_centrality
    assert CENTRALITY_MAPPING[Centrality.DEGREE] == degree_centrality
    assert CENTRALITY_MAPPING[Centrality.EIGENVECTOR] == eigenvector_centrality
    assert CENTRALITY_MAPPING[Centrality.PAGERANK] == pagerank
    assert CENTRALITY_MAPPING[Centrality.KATZ] == katz_centrality
    assert CENTRALITY_MAPPING[Centrality.HARMONIC] == harmonic_centrality
    assert CENTRALITY_MAPPING[Centrality.LOAD] == load_centrality
    assert (
        CENTRALITY_MAPPING[Centrality.CURRENT_FLOW_CLOSENESS]
        == current_flow_closeness_centrality
    )
    assert (
        CENTRALITY_MAPPING[Centrality.CURRENT_FLOW_BETWEENNESS]
        == current_flow_betweenness_centrality
    )
    assert CENTRALITY_MAPPING[Centrality.SUBGRAPH] == subgraph_centrality
    assert (
        CENTRALITY_MAPPING[Centrality.COMMUNICABILITY_BETWEENNESS]
        == communicability_betweenness_centrality
    )
    assert (
        CENTRALITY_MAPPING[Centrality.GROUP_BETWEENNESS] == group_betweenness_centrality
    )
    assert CENTRALITY_MAPPING[Centrality.GROUP_CLOSENESS] == group_closeness_centrality
    assert CENTRALITY_MAPPING[Centrality.GROUP_DEGREE] == group_degree_centrality
    assert CENTRALITY_MAPPING[Centrality.PERCOLATION] == percolation_centrality
    assert CENTRALITY_MAPPING[Centrality.SECOND_ORDER] == second_order_centrality
    assert CENTRALITY_MAPPING[Centrality.TROPHIC_LEVELS] == trophic_levels
    assert CENTRALITY_MAPPING[Centrality.LAPLACIAN] == laplacian_centrality
