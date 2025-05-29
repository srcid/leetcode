from weighted_graph_typing import *
from unionfind import UnionFind


def kruskal(graph: AdjacencyList) -> EdgesList:
    edges: EdgesList = [
        (node, neigh, cost)
        for node, adjacencies in graph.items()
        for neigh, cost in adjacencies
    ]
    edges.sort(key=lambda node_value: node_value[2])

    mst: EdgesList = []
    uf = UnionFind()

    for u, v, cost in edges:
        u_set = uf.find(u)
        v_set = uf.find(v)

        if u_set != v_set:
            mst.append((u, v, cost))
            uf.union(u_set, v_set)

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

    mst = kruskal(graph)

    print(mst)
