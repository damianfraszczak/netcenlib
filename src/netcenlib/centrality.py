import networkx as nx
from networkx import Graph

from netcenlib.algorithms.algebraic_centrality import algebraic_centrality
from netcenlib.algorithms.average_distance_centrality import \
    average_distance_centrality
from netcenlib.algorithms.barycenter_centrality import barycenter_centrality
from netcenlib.algorithms.bottle_neck_centrality import bottle_neck_centrality
from netcenlib.algorithms.centroid_centrality import centroid_centrality
from netcenlib.algorithms.cluster_rank_centrality import cluster_rank_centrality
from netcenlib.algorithms.coreness_centrality import coreness_centrality
from netcenlib.algorithms.decay_centrality import decay_centrality
from netcenlib.algorithms.diffusion_degree_centrality import \
    diffusion_degree_centrality
from netcenlib.algorithms.entropy_centrality import entropy_centrality
from netcenlib.algorithms.geodestic_k_path_centrality import \
    geodestic_k_path_centrality
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
    Centrality.DISPERSION: nx.dispersion,
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
    Centrality.VOTE_RANK: nx.voterank,

}


def compute_centrality(network, centrality: Centrality, *args, **kwargs):
    return CENTRALITY_MAPPING[centrality](network, *args, **kwargs)


class CentralityService:

    def __init__(self, network: Graph):
        self.network = network

    @property
    def degree(self):
        return nx.degree_centrality(self.network)

    @property
    def closeness(self):
        return nx.closeness_centrality(self.network)

    @property
    def betweenness(self):
        return nx.betweenness_centrality(self.network)

    @property
    def eigenvector(self):
        return nx.eigenvector_centrality(self.network)

    @property
    def pagerank(self):
        return nx.pagerank(self.network)

    @property
    def katz(self):
        return nx.katz_centrality(self.network)

    @property
    def harmonic(self):
        return nx.harmonic_centrality(self.network)

    @property
    def load(self):
        return nx.load_centrality(self.network)

    @property
    def current_flow_closeness(self):
        return nx.current_flow_closeness_centrality(self.network)

    @property
    def current_flow_betweenness(self):
        return nx.current_flow_betweenness_centrality(self.network)

    @property
    def subgraph(self):
        return nx.subgraph_centrality(self.network)

    @property
    def communicability_betweenness(self):
        return nx.communicability_betweenness_centrality(self.network)

    @property
    def group_betweenness(self):
        return nx.group_betweenness_centrality(self.network)

    @property
    def group_closeness(self):
        return nx.group_closeness_centrality(self.network)

    @property
    def group_degree(self):
        return nx.group_degree_centrality(self.network)

    @property
    def vote_rank(self):
        return nx.voterank(self.network)

    @property
    def dispersion(self):
        return nx.dispersion(self.network)

    @property
    def percolation(self):
        return nx.percolation_centrality(self.network)

    @property
    def second_order(self):
        return nx.second_order_centrality(self.network)

    @property
    def trophic_levels(self):
        return nx.trophic_levels(self.network)

    @property
    def laplacian(self):
        return nx.laplacian_centrality(self.network)

    # implementations from netcenlib
    @property
    def algebraic(self):
        return algebraic_centrality(self.network)

    @property
    def average_distance(self):
        return average_distance_centrality(self.network)

    @property
    def barycenter(self):
        return barycenter_centrality(self.network)

    @property
    def bottle_neck(self):
        return bottle_neck_centrality(self.network)

    @property
    def centroid(self):
        return centroid_centrality(self.network)

    @property
    def cluster_rank(self):
        return cluster_rank_centrality(self.network)

    @property
    def coreness(self):
        return coreness_centrality(self.network)

    @property
    def decay(self):
        return decay_centrality(self.network)

    @property
    def diffusion(self):
        return diffusion_degree_centrality(self.network)

    @property
    def entropy(self):
        return entropy_centrality(self.network)

    @property
    def geodestic(self):
        return geodestic_k_path_centrality(self.network)

    @property
    def heatmap(self):
        return heatmap_centrality(self.network)

    @property
    def leverage(self):
        return leverage_centrality(self.network)

    @property
    def lin(self):
        return lin_centrality(self.network)

    @property
    def mnc(self):
        return mnc_centrality(self.network)

    @property
    def pdi(self):
        return pdi_centrality(self.network)

    @property
    def radiality(self):
        return radiality_centrality(self.network)

    @property
    def rumor(self):
        return rumor_centrality(self.network)

    @property
    def semi_local(self):
        return semi_local_centrality(self.network)

    @property
    def topological(self):
        return topological_centrality(self.network)

    def compute_centrality(self, centrality: Centrality, *args, **kwargs):
        return compute_centrality(self.network, centrality, *args, **kwargs)
