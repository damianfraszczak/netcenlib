import networkx as nx


def algebraic_centrality(network, alpha=0.85, max_iter=100, tol=1.0e-6):
    """
    Calculate the Algebraic Centrality for each node in a network.

    Algebraic Centrality is a measure based on the concept of random walks and algebraic connectivity.
    It updates each node's centrality based on its neighbors' centralities, reflecting how information
    flows through the network.

    Parameters:
    network (NetworkX graph): The graph for which to calculate centrality.
    alpha (float): Damping factor representing the probability of continuing a random walk.
    max_iter (int): Maximum number of iterations for the algorithm.
    tol (float): Tolerance for convergence - the algorithm stops if changes are below this value.

    Returns:
    dict: A dictionary where keys are nodes and values are the centrality scores.

    Reference:
    "Algebraic Centrality" as described on CentiServer:
    https://www.centiserver.org/centrality/Algebraic_Centrality/
    """

    # Initialize centrality values
    centrality = {node: 1.0 / network.number_of_nodes() for node in network.nodes()}

    # Adjacency matrix
    A = nx.to_numpy_array(network)

    # Iterative process
    for _ in range(max_iter):
        previous_centrality = centrality.copy()

        for i, node in enumerate(network.nodes()):
            neighbor_sum = sum(A[i, j] * previous_centrality[n] for j, n in enumerate(network.nodes()))
            centrality[node] = (1 - alpha) + alpha * neighbor_sum

        # Check for convergence
        if all(abs(centrality[n] - previous_centrality[n]) < tol for n in network.nodes()):
            break

    return centrality
