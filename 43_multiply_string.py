from itertools import zip_longest


class SolutionIdeal:
    def multiply(self, num1: str, num2: str) -> str:
        return str(int(num1) * int(num2))


class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if "0" in (num1, num2):
            return "0"
        if "1" in (num1, num2):
            return num2 if num1 == "1" else num1

        ans = ""
        pts = []

        if len(num1) < len(num2):
            num1, num2 = num2, num1

        num1 = tuple(map(int, num1))
        num2 = tuple(map(int, num2))

        for pi, i in enumerate(reversed(num1)):
            r = 0
            pt = []
            for j in reversed(num2):
                aux = i * j + r
                r, aux = divmod(aux, 10)
                pt.append(aux)

            if r != 0:
                pt.append(r)

            pts.append(([0] * pi) + pt)

        r = 0
        for pt in zip_longest(*pts, fillvalue=0):
            d = sum(pt) + r
            r, d = divmod(d, 10)
            ans = str(d) + ans

        if r != 0:
            ans = str(r) + ans

        return ans


if __name__ == "__main__":
    num1 = "456"
    num2 = "123"
    s = Solution()
    ans = s.multiply(num1, num2)
    print(ans)

    num1 = "53"
    num2 = "72"
    s = Solution()
    ans = s.multiply(num1, num2)
    print(ans)
