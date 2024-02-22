# Quick Start Guide for NetCenLib

Welcome to NetCenLib, a comprehensive library for computing network centrality measures. This guide covers installation, basic usage, and visualization of centrality measures.

## Installation

Install NetCenLib using pip:

```bash
pip install netcenlib
```

## Basic Usage
NetCenLib offers two approaches for computing centrality measures: direct function calls and using the compute_centrality method with centrality enums.

### Direct Function Calls
Direct function calls are straightforward and ideal for simple applications:
```python
import networkx as nx
import netcenlib as ncl

# Create a graph
G = nx.karate_club_graph()

# Compute centrality measures
degree_centrality = ncl.degree_centrality(G)
betweenness_centrality = ncl.betweenness_centrality(G)
closeness_centrality = ncl.closeness_centrality(G)
eigenvector_centrality = ncl.eigenvector_centrality(G)
```
### Using `compute_centrality` method
The `compute_centrality` method is more flexible and allows for the computation of multiple centrality measures at once  or when iterating over multiple measures:
```python
from networkx import Graph
import networkx as nx
from netcenlib.centrality import compute_centrality
from netcenlib.taxonomies import Centrality

g: Graph = nx.karate_club_graph()
centrality_centroid = compute_centrality(g, Centrality.CENTROID)
```

### Visualization
You can visualize centrality measures using `matplotlib` and `networkx`:
```python
import matplotlib.pyplot as plt
import networkx as nx
import netcenlib as ncl

G = nx.karate_club_graph()
centrality = ncl.degree_centrality(G)

pos = nx.spring_layout(G)
sizes = [800 * v for v in centrality.values()]

nx.draw(G, pos, with_labels=True, node_size=sizes, edge_color="gray", alpha=0.4, linewidths=2)
plt.title("Degree Centrality Visualization")
plt.show()

```


If you would like to test ``NetCenLib`` functionalities without installing it on your machine consider using the preconfigured [Jupyter notebook](netcenlib.ipynb).
