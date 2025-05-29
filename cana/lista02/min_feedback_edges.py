from kruskal import kruskal
from weighted_graph_typing import *


def minfeedback(graph: AdjacencyList) -> EdgesList:
    igraph: AdjacencyList = {
        node: [(adj, -weight) for adj, weight in adjacencies]
        for node, adjacencies in graph.items()
    }

    mst = kruskal(igraph)

    edges: EdgesList = [
        (node, neigh, cost)
        for node, edges in graph.items()
        for neigh, cost in edges
        if (node, neigh, -cost) not in mst
    ]

    return edges


if __name__ == "__main__":
    graph: AdjacencyList = {
        1: [(4, 3), (6, 7), (8, 3), (10, 3)],
        2: [(9, 11), (10, 42), (12, 11)],
        3: [(7, 42), (11, 7)],
        5: [(6, 5)],
        7: [(9, 11), (10, 3), (11, 7)],
        8: [(11, 42)],
    }

    feedbacks = minfeedback(graph)

    print(feedbacks)
