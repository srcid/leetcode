# Dizemos que um vetor A[1, ..., n] tem um elemento majoritário se mais da metade dos
# seus elementos são iguais. Dado um vetor como entrada, escreva um algoritmo com
# complexidade O(n log n) para achar um elemento majoritário de um vetor e retorná-lo,
# ou indicar que o vetor não possui elemento majoritário. Na implementação deste
# algoritmo, a única operação de comparação permitida é para verificar pela igualdade
# entre elementos, ou seja, é possível usar A[i] = A[j], mas não é possível usar
# comparações de ordem como A[i] < A[j].

"""
Para ser majoritario deve haver (n // 2) + 1 elementos iguais.
n -- n // 2 + 1
1 -> 1 // 2 + 1 == 0 + 1 == 1
2 -> 2 // 2 + 1 == 1 + 1 == 2
3 -> 3 // 2 + 1 == 1 + 1 == 2
4 -> 4 // 2 + 1 == 2 + 1 == 3
5 -> 5 // 2 + 1 == 2 + 1 == 3
6 -> 6 // 2 + 1 == 3 + 1 == 4
7 -> 7 // 2 + 1 == 3 + 1 == 4

[2,1,1,1]
[1,2,1,3,1]
"""

from collections import defaultdict


def major_dp(A):
    d = defaultdict(int)

    for e in A:
        d[e] += 1

    for k, cnt in d.items():
        if cnt > len(A) // 2:
            return k

    return None


def major_linear(A):
    n = len(A)

    if n == 0:
        return None

    p = A[0]
    pc = 1

    for e in A[1:]:
        if pc == 0:
            p = e
            pc += 1
        elif e == p:
            pc += 1
        else:
            pc -= 1

    if pc > n // 2:
        return p

    return p if A.count(p) > n // 2 else None


def major_prob(A, n):
    match n:
        case 0:
            return None
        case 1:
            return A[0]

    p = A[0]

    l, r = [e for e in A if e == p], [e for e in A if e != p]

    if len(l) > n // 2:
        return p

    if len(r) > n // 2:
        return major_prob(r, n)

    return None


def major_aux(A, i, j):
    if (j - i) == 1:
        return A[i]

    k = i + (j - i) // 2

    ml = major_aux(A, i, k)
    mr = major_aux(A, k, j)

    if ml == mr:
        return ml

    return ml if A[i:j].count(ml) > A[i:j].count(mr) else mr


def major(A):
    if len(A) == 0:
        return None

    m = major_aux(A, 0, len(A))

    if m is None:
        return None

    return m if A.count(m) > (len(A) // 2) else None
