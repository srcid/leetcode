from copy import deepcopy

type Matrix = list[list[int]]


def mmul(A: Matrix, B: Matrix) -> Matrix:
    m = len(A)
    n = len(A[0])
    p = len(B[0])

    C = []

    for i in range(m):
        C.append([0] * p)
        for j in range(p):
            for k in range(n):
                C[i][j] += A[i][k] * B[k][j]

    return C


def mexp_naive(A: Matrix, exp: int) -> Matrix:
    if exp == 0:
        n = len(A)  # assuming square matrix
        E = [[1 if i == j else 0 for j in range(n)] for i in range(n)]
        return E

    E = deepcopy(A)

    while exp > 1:
        E = mmul(E, A)
        exp -= 1

    return E


def mexp(A: Matrix, exp: int) -> Matrix:
    match exp:
        case 0:
            n = len(A)  # assuming square matrix
            E = [[1 if i == j else 0 for j in range(n)] for i in range(n)]
            return E
        case 1:
            return A
        case 2:
            return mmul(A, A)

    if exp % 2 == 1:
        return mmul(A, mexp(mexp(A, 2), exp // 2))

    return mexp(mexp(A, 2), exp // 2)


def mexp_iti(A: Matrix, exp: int):
    n = len(A)  # assuming square matrix
    E = [[1 if i == j else 0 for j in range(n)] for i in range(n)]

    while exp >= 1:
        if exp % 2 == 1:  # is odd
            E = mmul(E, A)
        A = mmul(A, A)
        exp = exp // 2

    return E


def fib_iti(n: int) -> int:
    a, b = 0, 1

    for _ in range(n):
        a, b = b, a + b

    return a


def fib(n: int) -> int:
    A = [[0, 1], [1, 1]]
    B = [[0], [1]]

    return mmul(mexp(A, n), B)[0][0]
