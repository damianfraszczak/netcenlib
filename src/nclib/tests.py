import networkx as nx

from nclib.algorithms.semi_local_centrality import semi_local_centrality
from nclib.algorithms.topological_centrality import topological_centrality
from nclib.commons import print_dict

g = nx.karate_club_graph()

print_dict(topological_centrality(g))
