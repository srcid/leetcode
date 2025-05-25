# Para um conjunto de variáveis x1 ,..., xn , você recebe como entrada um conjunto
# de restrições de igualdade, da forma “xi == xj”, e um conjunto de restrições de
# desigualdade, da forma “xi  != xj ”. Escreva um algoritmo eficiente que recebe como
# entrada um conjunto m restrições sobre n variáveis e decide se todas as restrições
# podem ser satisfeitas.


def restric(n, eq, neq):
    def adjs(node):
        return [t[0] if t[0] != node else t[1] for t in eq if node in t]

    def bfs(node, components, color):
        components[node] = color
        q = adjs(node)

        while len(q) > 0:
            curNode, q = q[0], q[1:]
            components[curNode] = color
            q.extend([adj for adj in adjs(curNode) if components[adj] is None])

    components = [None for _ in range(n)]
    color = 0

    for i in range(n):
        if components[i] != None:
            continue

        bfs(i, components, color)
        color += 1

    for u, v in neq:
        if u == v:
            return False

        if components[u] == components[v]:
            return False

    return True


def restrict2(n, m):
    comp: list[set] = []

    for i in range(n):
        for s in comp:
            if i in s:
                s.add(i)
        comp.append(set([i]))

    

if __name__ == "__main__":
    n = 7
    eq = [(1, 3), (2, 3), (4, 5), (5, 6), (5, 6)]
    neq = [(5, 6)]

    ans = restric(n, eq, neq)

    print(ans)

    n = 7
    eq = [(1, 3), (2, 3), (4, 5), (5, 6), (5, 6)]
    neq = [(3, 4)]

    ans = restric(n, eq, neq)

    print(ans)
