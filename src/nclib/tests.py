import networkx as nx

from nclib.centrality import CentralityService
from nclib.commons import print_dict
from nclib.taxonomies import Centrality

g = nx.karate_club_graph()
centrality_service = CentralityService(g)

# for centrality in Centrality:
#     print("Centrality: ", centrality)
#     try:
#         print_dict(centrality_service.compute_centrality(centrality))
#     except Exception as e:
#         print(e)


print_dict(centrality_service.compute_centrality(Centrality.CENTROID))
print_dict(centrality_service.centroid)
