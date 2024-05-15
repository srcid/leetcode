from math import floor, sqrt


class SolutionLinear:
    def isPerfectSquare(self, num: int) -> bool:
        res = sqrt(num)
        return abs(res - floor(res)) <= 1e-8


class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num == 1:
            return True

        p, q = 2, num // 2

        if q < num / q:
            return False

        while p <= q:
            r = p + (q - p) // 2  # (p + q) / 2
            d = r - (num / r)  # (r * r) - num

            if abs(d) <= 1e-8:
                return True
            if d < 0:
                p = r + 1
            if d > 0:
                q = r - 1

        return False
