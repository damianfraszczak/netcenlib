import networkx as nx
from networkx import Graph

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
from netcenlib.taxonomies import Centrality

CENTRALITY_MAPPING = {
    Centrality.ALGEBRAIC: algebraic_centrality,
    Centrality.AVERAGE_DISTANCE: average_distance_centrality,
    Centrality.BARYCENTER: barycenter_centrality,
    Centrality.BETWEENNESS: nx.betweenness_centrality,
    Centrality.BOTTLE_NECK: bottle_neck_centrality,
    Centrality.CENTROID: centroid_centrality,
    Centrality.CLOSENESS: nx.closeness_centrality,
    Centrality.CLUSTER_RANK: cluster_rank_centrality,
    Centrality.COMMUNICABILITY_BETWEENNESS: nx.communicability_betweenness_centrality,
    Centrality.CORENESS: coreness_centrality,
    Centrality.CURRENT_FLOW_BETWEENNESS: nx.current_flow_betweenness_centrality,
    Centrality.CURRENT_FLOW_CLOSENESS: nx.current_flow_closeness_centrality,
    Centrality.DECAY: decay_centrality,
    Centrality.DEGREE: nx.degree_centrality,
    Centrality.DIFFUSION: diffusion_degree_centrality,
    Centrality.EIGENVECTOR: nx.eigenvector_centrality,
    Centrality.ENTROPY: entropy_centrality,
    Centrality.GEODESTIC: geodestic_k_path_centrality,
    Centrality.GROUP_BETWEENNESS: nx.group_betweenness_centrality,
    Centrality.GROUP_CLOSENESS: nx.group_closeness_centrality,
    Centrality.GROUP_DEGREE: nx.group_degree_centrality,
    Centrality.HARMONIC: nx.harmonic_centrality,
    Centrality.HEATMAP: heatmap_centrality,
    Centrality.KATZ: nx.katz_centrality,
    Centrality.LAPLACIAN: nx.laplacian_centrality,
    Centrality.LEVERAGE: leverage_centrality,
    Centrality.LIN: lin_centrality,
    Centrality.LOAD: nx.load_centrality,
    Centrality.MNC: mnc_centrality,
    Centrality.PAGERANK: nx.pagerank,
    Centrality.PDI: pdi_centrality,
    Centrality.PERCOLATION: nx.percolation_centrality,
    Centrality.RADIALITY: radiality_centrality,
    Centrality.RUMOR: rumor_centrality,
    Centrality.SECOND_ORDER: nx.second_order_centrality,
    Centrality.SEMI_LOCAL: semi_local_centrality,
    Centrality.SUBGRAPH: nx.subgraph_centrality,
    Centrality.TOPOLOGICAL: topological_centrality,
    Centrality.TROPHIC_LEVELS: nx.trophic_levels,
}


def compute_centrality(network, centrality: Centrality, *args, **kwargs):
    """Compute centrality measure for a given network."""
    return CENTRALITY_MAPPING[centrality](network, *args, **kwargs)


class CentralityService:

    def __init__(self, network: Graph):
        self.network = network

    @property
    def degree(self):
        return self.compute_centrality(Centrality.DEGREE)

    @property
    def closeness(self):
        return self.compute_centrality(Centrality.CLOSENESS)

    @property
    def betweenness(self):
        return self.compute_centrality(Centrality.BETWEENNESS)

    @property
    def eigenvector(self):
        return self.compute_centrality(Centrality.EIGENVECTOR)

    @property
    def pagerank(self):
        return self.compute_centrality(Centrality.PAGERANK)

    @property
    def katz(self):
        return self.compute_centrality(Centrality.KATZ)

    @property
    def harmonic(self):
        return self.compute_centrality(Centrality.HARMONIC)

    @property
    def load(self):
        return self.compute_centrality(Centrality.LOAD)

    @property
    def current_flow_closeness(self):
        return self.compute_centrality(Centrality.CURRENT_FLOW_CLOSENESS)

    @property
    def current_flow_betweenness(self):
        return self.compute_centrality(Centrality.CURRENT_FLOW_BETWEENNESS)

    @property
    def subgraph(self):
        return self.compute_centrality(Centrality.SUBGRAPH)

    @property
    def communicability_betweenness(self):
        return self.compute_centrality(Centrality.COMMUNICABILITY_BETWEENNESS)

    @property
    def group_betweenness(self):
        return self.compute_centrality(Centrality.GROUP_BETWEENNESS)

    @property
    def group_closeness(self):
        return self.compute_centrality(Centrality.GROUP_CLOSENESS)

    @property
    def group_degree(self):
        return self.compute_centrality(Centrality.GROUP_DEGREE)

    @property
    def percolation(self):
        return self.compute_centrality(Centrality.PERCOLATION)

    @property
    def second_order(self):
        return self.compute_centrality(Centrality.SECOND_ORDER)

    @property
    def trophic_levels(self):
        return self.compute_centrality(Centrality.TROPHIC_LEVELS)

    @property
    def laplacian(self):
        return self.compute_centrality(Centrality.LAPLACIAN)

    # implementations from netcenlib
    @property
    def algebraic(self):
        return self.compute_centrality(Centrality.ALGEBRAIC)

    @property
    def average_distance(self):
        return self.compute_centrality(Centrality.AVERAGE_DISTANCE)

    @property
    def barycenter(self):
        return self.compute_centrality(Centrality.BARYCENTER)

    @property
    def bottle_neck(self):
        return self.compute_centrality(Centrality.BOTTLE_NECK)

    @property
    def centroid(self):
        return self.compute_centrality(Centrality.CENTROID)

    @property
    def cluster_rank(self):
        return self.compute_centrality(Centrality.CLUSTER_RANK)

    @property
    def coreness(self):
        return self.compute_centrality(Centrality.CORENESS)

    @property
    def decay(self):
        return self.compute_centrality(Centrality.DECAY)

    @property
    def diffusion(self):
        return self.compute_centrality(Centrality.DIFFUSION)

    @property
    def entropy(self):
        return self.compute_centrality(Centrality.ENTROPY)

    @property
    def geodestic(self):
        return self.compute_centrality(Centrality.GEODESTIC)

    @property
    def heatmap(self):
        return self.compute_centrality(Centrality.HEATMAP)

    @property
    def leverage(self):
        return self.compute_centrality(Centrality.LEVERAGE)

    @property
    def lin(self):
        return self.compute_centrality(Centrality.LIN)

    @property
    def mnc(self):
        return self.compute_centrality(Centrality.MNC)

    @property
    def pdi(self):
        return self.compute_centrality(Centrality.PDI)

    @property
    def radiality(self):
        return self.compute_centrality(Centrality.RADIALITY)

    @property
    def rumor(self):
        return self.compute_centrality(Centrality.RUMOR)

    @property
    def semi_local(self):
        return self.compute_centrality(Centrality.SEMI_LOCAL)

    @property
    def topological(self):
        return self.compute_centrality(Centrality.TOPOLOGICAL)

    def compute_centrality(self, centrality: Centrality, *args, **kwargs):
        return compute_centrality(self.network, centrality, *args, **kwargs)
