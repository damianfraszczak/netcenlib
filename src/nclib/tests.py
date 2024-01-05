import networkx as nx

from nclib.algorithms.diffusion_degree import diffusion_degree
from nclib.algorithms.entropy_centrality import entropy_centrality
from nclib.commons import print_dict

g = nx.karate_club_graph()

print_dict(entropy_centrality(g))
