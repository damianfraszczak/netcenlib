from enum import Enum


class Centrality(Enum):
    """A list of centrality algorithms."""

    ALGEBRAIC = "algebraic"
    AVERAGE_DISTANCE = "average_distance"
    BARYCENTER = "barycenter"
    BETWEENNESS = "betweenness"
    BOTTLE_NECK = "bottle_neck"
    CENTROID = "centroid"
    CLOSENESS = "closeness"
    CLUSTER_RANK = "cluster_rank"
    COMMUNICABILITY_BETWEENNESS = "communicability_betweenness"
    CORENESS = "coreness"
    CURRENT_FLOW_BETWEENNESS = "current_flow_betweenness"
    CURRENT_FLOW_CLOSENESS = "current_flow_closeness"
    DECAY = "decay"
    DEGREE = "degree"
    DIFFUSION_DEGREE = "diffusion_degree"
    ECCENTRICITY = "eccentricity"
    EIGENVECTOR = "eigenvector"
    ENTROPY = "entropy"
    GEODESTIC_K_PATH = "geodestic_k_path"
    GROUP_BETWEENNESS = "group_betweenness"
    GROUP_CLOSENESS = "group_closeness"
    GROUP_DEGREE = "group_degree"
    HARMONIC = "harmonic"
    HEATMAP = "heatmap"
    HUBBELL = "hubbell"
    KATZ = "katz"
    LAPLACIAN = "laplacian"
    LEVERAGE = "leverage"
    LIN = "lin"
    LOAD = "load"
    MNC = "mnc"
    PAGERANK = "pagerank"
    PDI = "pdi"
    PERCOLATION = "percolation"
    RADIALITY = "radiality"
    RUMOR = "rumor"
    SECOND_ORDER = "second_order"
    SEMI_LOCAL = "semi_local"
    SUBGRAPH = "subgraph"
    TOPOLOGICAL = "topological"
    TROPHIC_LEVELS = "trophic_levels"
