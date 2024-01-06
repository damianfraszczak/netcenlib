import networkx as nx

from nclib.algorithms.heatmap_centrality import heatmap_centrality
from nclib.commons import print_dict

g = nx.karate_club_graph()

print_dict(heatmap_centrality(g))
