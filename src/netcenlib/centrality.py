"""Centrality measures for networks."""

import networkx as nx
from networkx import Graph

from netcenlib.algorithms import (
    algebraic_centrality,
    average_distance_centrality,
    barycenter_centrality,
    bottle_neck_centrality,
    centroid_centrality,
    cluster_rank_centrality,
    coreness_centrality,
    decay_centrality,
    diffusion_degree_centrality,
    entropy_centrality,
    geodestic_k_path_centrality,
    heatmap_centrality,
    hubbell_centrality,
    leverage_centrality,
    lin_centrality,
    mnc_centrality,
    pdi_centrality,
    radiality_centrality,
    rumor_centrality,
    semi_local_centrality,
    topological_centrality,
)
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
    Centrality.HUBBELL: hubbell_centrality,
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
    def hubbell(self):
        return self.compute_centrality(Centrality.HUBBELL)

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
