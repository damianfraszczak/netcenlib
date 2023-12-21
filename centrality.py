import networkx as nx
from networkx import Graph


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
