import networkx as nx

from src.algorithms.diffusion_degree import diffusion_degree
from src.commons import print_dict

g = nx.karate_club_graph()

print_dict(diffusion_degree(g))
