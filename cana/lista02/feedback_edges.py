def feedbacks(graph):
    visited = [0] * len(graph)
    fb = []

    def dfs(node):
        if visited[node - 1]:
            return True

        visited[node - 1] = 1

        for adj in graph[node]:
            if dfs(adj):
                fb.append((node, adj))

        return False

    for node in graph:
        if visited[node - 1] == 0:
            dfs(node)

    return fb


if __name__ == "__main__":
    graph = {
        1: [2, 3],
        2: [4, 5],
        3: [9],
        4: [6],
        5: [8],
        6: [7],
        7: [4],
        8: [1],
        9: [10],
        10: [1],
    }

    ans = feedbacks(graph)

    print(ans)
