import networkx as nx


def algebraic_centrality(network, alpha=0.85, max_iter=100, tol=1.0e-6):
    """
                Compute the Algebraic Centrality for each node in the graph G.
                Ref:  https://www.centiserver.org/centrality/Algebraic_Centrality/

                :param network: NetworkX graph
                :param alpha: Damping factor representing the probability of continuing a random walk.
                :param max_iter: Maximum number of iterations for the algorithm.
                :param tol: Tolerance for convergence - the algorithm stops if changes are below this value.
                :return: Dictionary of nodes with Rumor Centrality as the value
        """

    centrality = {node: 1.0 / network.number_of_nodes() for node in
                  network.nodes()}

    A = nx.to_numpy_array(network)

    for _ in range(max_iter):
        previous_centrality = centrality.copy()

        for i, node in enumerate(network.nodes()):
            neighbor_sum = sum(A[i, j] * previous_centrality[n] for j, n in
                               enumerate(network.nodes()))
            centrality[node] = (1 - alpha) + alpha * neighbor_sum

        if all(abs(centrality[n] - previous_centrality[n]) < tol for n in
               network.nodes()):
            break

    return centrality
