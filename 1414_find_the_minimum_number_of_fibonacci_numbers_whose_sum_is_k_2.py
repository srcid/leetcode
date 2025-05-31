import math


def bif(fn: int) -> int:
    phi = (1 + 5**0.5) / 2
    return math.ceil(math.log(fn * 5**0.5, phi))


def fib(n: int) -> int:
    return round(((1 + 5**0.5) / 2) ** n / 5**0.5)


class Solution:
    def findMinFibonacciNumbers(self, k: int) -> int:
        cnt = 0

        while k > 0:
            n = bif(k)
            a = fib(n)

            if a > k:
                a = fib(n - 1)

            k -= a
            cnt += 1

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
