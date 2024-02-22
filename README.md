# NetCenLib

NetCenLib (Network centrality library) is a tool to compute a wide range of centrality measures for a given network. The
library is designed to work with Python Networkx library.

## Overview

The goal of NetCenLib is to offer a comprehensive repository for implementing a broad spectrum of centrality measures. Each
year, new measures are introduced through scientific papers, often with only pseudo-code descriptions, making it
difficult for researchers to evaluate and compare them with existing methods. While implementations of well-known
centrality measures exist, recent innovations are frequently absent. NetCenLib strives to bridge this gap. It references the
renowned CentiServer portal for well-known centrality measures and their originating papers, aiming to encompass all
these measures in the future.

## Code structure

All custom implementations are provided under `netcenlib/algorithms` package. Each centrality measure is implemented in a separate file, named after the measure itself. Correspondingly, each file contains a function, named identically to the file, which calculates the centrality measure. This function accepts a NetworkX graph as input (and other params if applicable) and returns a dictionary, mapping nodes to their centrality values. Ultimately, every custom implementation is made available through the `netcenlib/algorithms` package.
## Implemented centrality measures:

- [Algebraic](https://www.centiserver.org/centrality/Algebraic_Centrality/)
- [Average Distance](https://www.centiserver.org/centrality/Average_Distance/)
- [Barycenter](https://www.centiserver.org/centrality/Barycenter_Centrality/)
- [Betweenness](https://www.centiserver.org/centrality/Shortest-Paths_Betweenness_Centrality/)
- [BottleNeck]( https://www.centiserver.org/centrality/BottleNeck/)
- [Centroid](https://www.centiserver.org/centrality/Centroid_value/)
- [Closeness](https://www.centiserver.org/centrality/Closeness_Centrality/)
- [ClusterRank](https://www.centiserver.org/centrality/ClusterRank/)
- [Communicability Betweenness](https://www.centiserver.org/centrality/Communicability_Betweenness_Centrality/)
- [Coreness](https://www.centiserver.org/centrality/Coreness_Centrality/)
- [Current Flow Betweenness](https://www.centiserver.org/centrality/Current-Flow_Betweenness_Centrality/)
- [Current Flow Closeness](https://www.centiserver.org/centrality/Current-Flow_Closeness_Centrality/)
- [Decay](https://www.centiserver.org/centrality/Decay_Centrality/)
- [Degree](https://www.centiserver.org/centrality/Degree_Centrality/)
- [Diffusion degree](https://www.centiserver.org/centrality/Diffusion_Degree/)
- [Eigenvector](https://www.centiserver.org/centrality/Eigenvector_Centrality/)
- [Entropy](https://www.centiserver.org/centrality/Entropy_Centrality/)
- [Geodestic k path](https://www.centiserver.org/centrality/Geodesic_K-Path_Centrality/)
- [Group Betweenness Centrality](https://www.centiserver.org/centrality/Group_Betweenness_Centrality/) - `netcenlib.algorithms.group_betweenness_centrality`
- [Group Closeness](https://networkx.org/documentation/stable/reference/algorithms/generated/networkx.algorithms.centrality.group_closeness_centrality.html) - `netcenlib.algorithms.group_closeness_centrality`
- [Group Degree](https://networkx.org/documentation/stable/reference/algorithms/generated/networkx.algorithms.centrality.group_degree_centrality.html) - `netcenlib.algorithms.group_degree_centrality`
- [Harmonic](https://www.centiserver.org/centrality/Harmonic_Centrality/)
- [Heatmap](https://www.centiserver.org/centrality/Heatmap_Centrality/)
- [Katz](https://www.centiserver.org/centrality/Katz_Centrality/)
- [Hubbell](https://www.centiserver.org/centrality/Hubbell_Centrality/)
- [Laplacian](https://www.centiserver.org/centrality/Laplacian_Centrality/)
- [Leverage](https://www.centiserver.org/centrality/Leverage_Centrality/)
- [Lin](https://www.centiserver.org/centrality/Lin_Centrality/)
- [Load](https://www.centiserver.org/centrality/Load_Centrality/)
- [Mnc](https://www.centiserver.org/centrality/MNC_Maximum_Neighborhood_Component/)
- [Pagerank](https://www.centiserver.org/centrality/PageRank/)
- [Pdi](https://www.centiserver.org/centrality/Pairwise_Disconnectivity_Index/)
- [Percolation](https://www.centiserver.org/centrality/Percolation_Centrality/)
- [Radiality](https://www.centiserver.org/centrality/Radiality_Centrality/)
- [Rumor](https://www.centiserver.org/centrality/Rumor_Centrality/)
- [Second Order](https://www.centiserver.org/centrality/Second_Order_Centrality/)
- [Semi Local](https://www.centiserver.org/centrality/Semi_Local_Centrality/)
- [Subgraph](https://www.centiserver.org/centrality/Subgraph_Centrality/)
- [Topological](https://www.centiserver.org/centrality/Topological_Coefficient/)
- [Trophic Levels](https://networkx.org/documentation/stable/reference/algorithms/generated/networkx.algorithms.centrality.trophic_levels.html) - `netcenlib.algorithms.trophic_levels_centrality`

## How to use
Library can be installed using pip:

```bash
pip install netcenlib
```

## Code usage

Provided algorithms can be executed in the following ways:

- by invoking a specific function from `netcenlib.algorithms` package, which computes a given centrality measure for a
  given graph.

```python
import networkx as nx
import netcenlib as ncl

# Create a graph
G = nx.karate_club_graph()

# Compute degree centrality
degree_centrality = ncl.degree_centrality(G)

# Compute betweenness centrality
betweenness_centrality = ncl.betweenness_centrality(G)

# Compute closeness centrality
closeness_centrality = ncl.closeness_centrality(G)

# Compute eigenvector centrality
eigenvector_centrality = ncl.eigenvector_centrality(G)
```

- invoking `compute_centrality` method of `CentralityService` class, which allows to compute centrality for a given
  centrality measure.

```python
from typing import Any
import networkx as nx
from networkx import Graph

from netcenlib.centrality import compute_centrality
from netcenlib.taxonomies import Centrality

g: Graph = nx.karate_club_graph()
centrality_centroid: dict[Any, float] = compute_centrality(g, Centrality.CENTROID)
```

This method allows you not to directly specify centrality, making it easy to compute different centralities in a loop.

## Contributing

For contributing, refer to its [CONTRIBUTING.md](.github/CONTRIBUTING.md) file.
We are a welcoming community... just follow the [Code of Conduct](.github/CODE_OF_CONDUCT.md).

## Maintainers

Project maintainers are:

- Damian Frąszczak
- Edyta Frąszczak
