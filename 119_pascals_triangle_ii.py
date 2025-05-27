from functools import cache
from math import factorial as real_factorial
from typing import List


@cache
def factorial(n):
    return real_factorial(n)


def binon(p, q):
    return factorial(p) // (factorial(p - q) * factorial(q))


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex <= 1:
            return [[1], [1, 1]][rowIndex]

        M = rowIndex // 2 + 1
        ans = [1] * M

        for i in range(1, M):
            ans[i] = binon(rowIndex, i)

        return ans + ans[::-1] if rowIndex % 2 else ans[:-1] + ans[::-1]
