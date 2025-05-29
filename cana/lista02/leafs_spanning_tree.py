from kruskal import kruskal
from unionfind import UnionFind
from weighted_graph_typing import *


def leafs_spanning_tree(graph: AdjacencyList, leafs: list[Node]):
    # removing leafs from graph
    graph_leafless: AdjacencyList = {
        node: [(neigh, cost) for neigh, cost in adjacencies if neigh not in leafs]
        for node, adjacencies in graph.items()
        if node not in leafs
    }

    # List of edges with the leafs nodes as one of their ends
    leafs_edges: EdgesList = [
        (node, neigh, cost)
        for node, adjacencies in graph.items()
        for neigh, cost in adjacencies
        if neigh in leafs or node in leafs
    ]

    # sorting leafs edges by cost
    leafs_edges.sort(key=lambda node_neigh_cost: node_neigh_cost[2])

    mst = kruskal(graph_leafless)
    uf = UnionFind()

    for u, v, cost in leafs_edges:
        u_set = uf.exists(u)
        v_set = uf.exists(v)

        if u_set == None and v_set == None:
            uf.addset({u, v})
            mst.append((u, v, cost))

    return mst


if __name__ == "__main__":
    graph: AdjacencyList = {
        1: [(4, 3), (6, 7), (8, 3), (10, 3)],
        2: [(9, 11), (10, 42), (12, 11)],
        3: [(7, 42), (11, 7)],
        5: [(6, 5)],
        7: [(9, 11), (10, 3), (11, 7)],
        8: [(11, 42)],
    }

    mst = leafs_spanning_tree(graph, [9, 11])

    print(mst)
