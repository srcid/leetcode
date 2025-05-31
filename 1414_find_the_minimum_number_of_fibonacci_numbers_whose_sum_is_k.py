import math
from functools import cache


def bif(fn: int) -> int:
    """Inverse FIBonacci function

    considering log as base phi, log(phi) = 1
    fn                           ~= phi**n / math.sqrt(5)
    fn / sqrt(5)                 ~= phi**n
    log(fn / sqrt(5))            ~= log(phi**n)
    log(fn / sqrt(5))            ~= n * log(phi)
    log(fn / sqrt(5)) / log(phi) ~= n
    log(fn / sqrt(5))            ~= n
    log(fn) - log(sqrt(5))       ~= n

    Args:
        fn (int): nth number of fibonacci

    Returns:
        int: approximated n index of fibonacci function
    """

    phi = (1 + math.sqrt(5)) / 2
    return math.ceil(math.log(fn, phi) + math.log(math.sqrt(5), phi))


@cache
def mmul(A, B):
    m, n, p = len(A), len(B), len(B[0])

    return tuple(
        tuple(sum(A[i][k] * B[k][j] for k in range(n)) for j in range(p))
        for i in range(m)
    )


@cache
def mexp(matrix, e):
    N = len(matrix)
    base = matrix
    ans = tuple(tuple(([0] * i) + [1] + ([0] * (N - (i + 1)))) for i in range(N))

    if e == 0:
        return ans
    if e == 1:
        return base

    while e:
        if e % 2:  # odd
            ans = mmul(ans, base)
            e -= 1

        base = mmul(base, base)

        e //= 2

    return ans


def fib(n):
    fmatrix = mexp(((0, 1), (1, 1)), n)
    ans = mmul(fmatrix, ((0,), (1,)))
    return ans[0][0]


class Solution:

    def findMinFibonacciNumbers(self, k: int) -> int:
        cnt = 0
        n = bif(k)
        a, b = fib(n + 1), fib(n)

        while k > 0 and a != 0:
            if k - a >= 0:
                cnt += 1
                k = k - a
            a, b = b, a - b

        return cnt


if __name__ == "__main__":
    s = Solution()

    for k, expected in (
        (7, 2),
        (10, 2),
        (19, 3),
        (21, 1),
        (22, 2),
        (49, 3),
        (100, 3),
    ):
        ans = s.findMinFibonacciNumbers(k)
        print(f"{k=} -> {ans=} --- {expected=}")
