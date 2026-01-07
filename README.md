# NetCenLib


<h1 align="center">
    ⚔️ NetCenLib (Network centrality library) ⚔️
</h1>

<p align="center">
    <img alt="PyPI - Python Version" src="https://img.shields.io/pypi/pyversions/netcenlib.svg">
    <img alt="PyPI - Downloads" src="https://img.shields.io/pypi/dm/netcenlib.svg" href="https://pepy.tech/project/netcenlib">
    <a href="https://repology.org/project/python:netcenlib/versions">
        <img src="https://repology.org/badge/tiny-repos/python:netcenlib.svg" alt="Packaging status">
    </a>
    <img alt="Downloads" src="https://pepy.tech/badge/netcenlib">
    <img alt="GitHub license" src="https://img.shields.io/github/license/damianfraszczak/netcenlib.svg" href="https://github.com/damianfraszczak/netcenlib/blob/master/LICENSE">
    <img alt="Documentation Status" src="https://readthedocs.org/projects/netcenlib/badge/?version=latest" href="https://netcenlib.readthedocs.io/en/latest/?badge=latest">
</p>


NetCenLib (Network centrality library) is a tool to compute a wide range of centrality measures for a given network. The
library is designed to work with Python Networkx library.

If you use _NetCenLib_ as support to your research consider citing:

`D. Frąszczak, E. Frąszczak. NetCenLib: A comprehensive python library for network centrality analysis and evaluation. SoftwareX. 2024.` [DOI:10.1016/j.softx.2024.101699](https://doi.org/10.1016/j.softx.2024.101699)

[RG paper](https://www.researchgate.net/publication/380253577_NetCenLib_A_comprehensive_python_library_for_network_centrality_analysis_and_evaluation)


## Overview

The goal of NetCenLib is to offer a comprehensive repository for implementing a broad spectrum of centrality measures. Each
year, new measures are introduced through scientific papers, often with only pseudo-code descriptions, making it
difficult for researchers to evaluate and compare them with existing methods. While implementations of well-known
centrality measures exist, recent innovations are frequently absent. NetCenLib strives to bridge this gap. It references the
renowned CentiServer portal for well-known centrality measures and their originating papers, aiming to encompass all
these measures in the future.

## Code structure

All custom implementations are provided under `netcenlib/algorithms` package. Each centrality measure is implemented in a separate file, named after the measure itself. Correspondingly, each file contains a function, named identically to the file, which calculates the centrality measure. This function accepts a NetworkX graph as input (and other params if applicable) and returns a dictionary, mapping nodes to their centrality values. Ultimately, every custom implementation is made available through the `netcenlib/algorithms` package.

## Implemented centrality measures

- [Algebraic](https://www.centiserver.ir/centrality/Algebraic_Centrality/)
- [Average Distance](https://www.centiserver.ir/centrality/Average_Distance/)
- [Barycenter](https://www.centiserver.ir/centrality/Barycenter_Centrality/)
- [Betweenness](https://www.centiserver.ir/centrality/Shortest-Paths_Betweenness_Centrality/)
- [BottleNeck]( https://www.centiserver.ir/centrality/BottleNeck/)
- [Centroid](https://www.centiserver.ir/centrality/Centroid_value/)
- [Closeness](https://www.centiserver.ir/centrality/Closeness_Centrality/)
- [ClusterRank](https://www.centiserver.ir/centrality/ClusterRank/)
- [Communicability Betweenness](https://www.centiserver.ir/centrality/Communicability_Betweenness_Centrality/)
- [Coreness](https://www.centiserver.ir/centrality/Coreness_Centrality/)
- [Current Flow Betweenness](https://www.centiserver.ir/centrality/Current-Flow_Betweenness_Centrality/)
- [Current Flow Closeness](https://www.centiserver.ir/centrality/Current-Flow_Closeness_Centrality/)
- [Decay](https://www.centiserver.ir/centrality/Decay_Centrality/)
- [Degree](https://www.centiserver.ir/centrality/Degree_Centrality/)
- [Diffusion degree](https://www.centiserver.ir/centrality/Diffusion_Degree/)
- [Eccentricity](https://networkx.org/documentation/stable/reference/algorithms/generated/networkx.algorithms.distance_measures.eccentricity.html)
- [Eigenvector](https://www.centiserver.ir/centrality/Eigenvector_Centrality/)
- [Entropy](https://www.centiserver.ir/centrality/Entropy_Centrality/)
- [Geodestic k path](https://www.centiserver.ir/centrality/Geodesic_K-Path_Centrality/)
- [Group Betweenness Centrality](https://www.centiserver.ir/centrality/Group_Betweenness_Centrality/)
- [Group Closeness](https://networkx.org/documentation/stable/reference/algorithms/generated/networkx.algorithms.centrality.group_closeness_centrality.html)
- [Group Degree](https://networkx.org/documentation/stable/reference/algorithms/generated/networkx.algorithms.centrality.group_degree_centrality.html)
- [Harmonic](https://www.centiserver.ir/centrality/Harmonic_Centrality/)
- [Heatmap](https://www.centiserver.ir/centrality/Heatmap_Centrality/)
- [Katz](https://www.centiserver.ir/centrality/Katz_Centrality/)
- [Hubbell](https://www.centiserver.ir/centrality/Hubbell_Centrality/)
- [Laplacian](https://www.centiserver.ir/centrality/Laplacian_Centrality/)
- [Leverage](https://www.centiserver.ir/centrality/Leverage_Centrality/)
- [Lin](https://www.centiserver.ir/centrality/Lin_Centrality/)
- [Load](https://www.centiserver.ir/centrality/Load_Centrality/)
- [Mnc](https://www.centiserver.ir/centrality/MNC_Maximum_Neighborhood_Component/)
- [Pagerank](https://www.centiserver.ir/centrality/PageRank/)
- [Pdi](https://www.centiserver.ir/centrality/Pairwise_Disconnectivity_Index/)
- [Percolation](https://www.centiserver.ir/centrality/Percolation_Centrality/)
- [Radiality](https://www.centiserver.ir/centrality/Radiality_Centrality/)
- [Rumor](https://www.centiserver.ir/centrality/Rumor_Centrality/)
- [Second Order](https://www.centiserver.ir/centrality/Second_Order_Centrality/)
- [Semi Local](https://www.centiserver.ir/centrality/Semi_Local_Centrality/)
- [Subgraph](https://www.centiserver.ir/centrality/Subgraph_Centrality/)
- [Topological](https://www.centiserver.ir/centrality/Topological_Coefficient/)
- [Trophic Levels](https://networkx.org/documentation/stable/reference/algorithms/generated/networkx.algorithms.centrality.trophic_levels.html)

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

This method allows you not to directly specify centrality, making it easy to compute different centralises in a loop.

For more examples and details, please refer to the [official documentation](https://netcenlib.readthedocs.io/en/latest/index.html).

## Contributing

For contributing, refer to its [CONTRIBUTING.md](.github/CONTRIBUTING.md) file.
We are a welcoming community... just follow the [Code of Conduct](.github/CODE_OF_CONDUCT.md).

## Maintainers

Project maintainers are:

- Damian Frąszczak
- Edyta Frąszczak
