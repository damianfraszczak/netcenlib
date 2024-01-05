import networkx as nx

from src.algorithms.diffusion_degree import diffusion_degree
from src.algorithms.entropy_centrality import entropy_centrality
from src.commons import print_dict

g = nx.karate_club_graph()

print_dict(entropy_centrality(g))
