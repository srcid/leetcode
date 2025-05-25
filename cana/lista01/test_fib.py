import pytest
from fib import Matrix, fib, fib_iti, mexp, mexp_iti, mexp_naive, mmul

# helper functions


def mcomp(A: Matrix, B: Matrix):
    m, n = len(A), len(A[0])
    p, q = len(B), len(B[0])

    if m != p or n != q:
        return False

    for ra, rb in zip(A, B):
        for ea, eb in zip(ra, rb):
            if ea != eb:
                return False

    return True


def identity_matrix(n):
    """Utility to generate an n x n identity matrix."""
    return [[1 if i == j else 0 for j in range(n)] for i in range(n)]


# matrix multiplication


@pytest.mark.parametrize(
    "A, B, expected",
    [
        (
            [[1, 2], [3, 4]],
            [[5, 6], [7, 8]],
            [[19, 22], [43, 50]],
        ),
        (
            [[1, 2, 3], [4, 5, 6]],
            [[7, 8], [9, 10], [11, 12]],
            [[58, 64], [139, 154]],
        ),
        (
            [[3]],
            [[7]],
            [[21]],
        ),
        (
            [[0, 0], [0, 0]],
            [[1, 2], [3, 4]],
            [[0, 0], [0, 0]],
        ),
        (
            [[1, 0], [0, 1]],
            [[5, 6], [7, 8]],
            [[5, 6], [7, 8]],
        ),
    ],
)
def test_mmul_valid_cases(A, B, expected):
    assert mmul(A, B) == expected


# matrix exponentiation

mexp_cases = [
    ([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 0, [[1, 0, 0], [0, 1, 0], [0, 0, 1]]),
    ([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 1, [[1, 2, 3], [4, 5, 6], [7, 8, 9]]),
    ([[2, 0], [0, 2]], 2, [[4, 0], [0, 4]]),
    ([[1, 1], [1, 0]], 3, [[3, 2], [2, 1]]),  # Known from Fibonacci Q-matrix
    ([[5]], 3, [[125]]),
    ([[2, 3], [1, 4]], 0, identity_matrix(2)),
]


## naive


@pytest.mark.parametrize("A, exp, expected", mexp_cases)
def test_mexp_naive_valid_cases(A, exp, expected):
    assert mexp_naive(A, exp) == expected


def test_mexp_naive_identity_power_one():
    A = identity_matrix(3)
    assert mexp_naive(A, 1) == identity_matrix(3)


def test_mexp_naive_large_power():
    A = [[1, 1], [1, 0]]
    result = mexp_naive(A, 10)
    expected = [[89, 55], [55, 34]]  # Fibonacci Q-matrix raised to 10
    assert result == expected


## mexp


@pytest.mark.parametrize("A, exp, expected", mexp_cases)
def test_mexp_valid_cases(A, exp, expected):
    assert mexp(A, exp) == expected


@pytest.mark.skip
def test_mexp_identity_power_one():
    A = identity_matrix(3)
    assert mexp(A, 1) == identity_matrix(3)


@pytest.mark.skip
def test_mexp_large_power():
    A = [[1, 1], [1, 0]]
    result = mexp(A, 10)
    expected = [[89, 55], [55, 34]]  # Fibonacci Q-matrix raised to 10
    assert result == expected


## mexp_iti


@pytest.mark.parametrize("A, exp, expected", mexp_cases)
def test_mexp_iti_valid_cases(A, exp, expected):
    assert mexp_iti(A, exp) == expected


def test_mexp_iti_identity_power_one():
    A = identity_matrix(3)
    assert mexp_iti(A, 1) == identity_matrix(3)


def test_mexp_iti_large_power():
    A = [[1, 1], [1, 0]]
    result = mexp_iti(A, 10)
    expected = [[89, 55], [55, 34]]  # Fibonacci Q-matrix raised to 10
    assert result == expected


# Testing fibonacci


@pytest.mark.parametrize("n", [0, 1, 2, 3, 4, 5, 6, 50, 100, 101])
def test_fib(n):
    assert fib(n) == fib_iti(n)
