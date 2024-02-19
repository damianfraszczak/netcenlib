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

All custom implementations are provided under `netcenlib/algorithms` package.

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
- [Group Betweenness](https://www.centiserver.org/centrality/Group_Betweenness_Centrality/)
- Group Closeness
- Group Degree
- [Harmonic](https://www.centiserver.org/centrality/Harmonic_Centrality/)
- [Heatmap](https://www.centiserver.org/centrality/Heatmap_Centrality/)
- [Katz](https://www.centiserver.org/centrality/Katz_Centrality/)
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
- Trophic Levels

## How to use
Library can be installed using pip:

```bash
pip install netcenlib
```

## Code usage

Provided algorithms can be executed in the following ways:

- by importing and using specific method:

```python
from typing import Any
import networkx as nx
from networkx import Graph
from netcenlib.algorithms.algebraic_centrality import algebraic_centrality
```

- using the `CentralityService` class, which provides access to all centralities through its properties.

```python
from typing import Any
import networkx as nx
from networkx import Graph
from netcenlib.centrality import CentralityService

g: Graph = nx.karate_club_graph()
centrality_service = CentralityService(g)
centrality_centroid: dict[Any, float] = centrality_service.centroid
```

The biggest advantage of using `CentralityService` class is that it allows to compute all centralities at once. Users
have all implementations within reach

- invoking `compute_centrality` method of `CentralityService` class, which allows to compute centrality for a given
  centrality measure.

```python
import networkx as nx
from networkx import Graph

from netcenlib.centrality import compute_centrality
from netcenlib.taxonomies import Centrality

g: Graph = nx.karate_club_graph()
centrality_centroid: dict[Any, float] = compute_centrality(g, Centrality.CENTROID)
```

This method allows you not to directly specify centrality, making it easy to compute different centralities in a loop.

## Contributing

For contributing, refer to its [CONTRIBUTING.md](CONTRIBUTING.md) file.

## Maintainers

Project maintainers are:

- Damian Frąszczak
- Edyta Frąszczak
