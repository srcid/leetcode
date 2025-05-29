from typing import List


# This solution exceeds the time limit for the problem
class Solution:
    def adjs(self, row: int, col: int):
        return (
            (a, b)
            for a, b in ((row + 1, col), (row, col + 1), (row + 1, col + 1))
            if 0 <= a < self.M and 0 <= b < self.N
        )

    def expand_sqr(self, sqr) -> list[tuple[int, int]] | None:
        next_sqr = []

        for p, q in sqr:
            for a, b in self.adjs(p, q):
                if (a, b) not in sqr and (a, b) not in next_sqr:
                    if self.matrix[a][b] == "1":
                        next_sqr.append((a, b))
                    else:
                        return None

        return next_sqr if len(next_sqr) == len(sqr) + 2 else None

    def bfs(self, i: int, j: int) -> int:
        sqr = [(i, j)]
        n = 0

        while True:
            next_sqr = self.expand_sqr(sqr)
            n += 1

            if next_sqr:
                sqr = next_sqr
            else:
                break

        return n

    def maximalSquare(self, matrix: List[List[str]]) -> int:
        self.M, self.N = len(matrix), len(matrix[0])
        self.matrix = matrix
        maximal = 0

        for i in range(self.M):
            for j in range(self.N):
                if self.matrix[i][j] == "1":
                    cr = i + 1

                    while cr < self.M and self.matrix[cr][j] == "1":
                        cr += 1

                    cc = j + 1

                    while cc < self.N and self.matrix[i][cc] == "1":
                        cc += 1

                    if min(cr - i, cc - j) ** 2 <= maximal:
                        continue

                    n = self.bfs(i, j)
                    maximal = max(maximal, n**2)
        return maximal


if __name__ == "__main__":
    s = Solution()

    matrix = [
        ["1", "0", "1", "0", "0"],
        ["1", "0", "1", "1", "1"],
        ["1", "1", "1", "1", "1"],
        ["1", "0", "0", "1", "0"],
    ]

    ans = s.maximalSquare(matrix)
    print(ans, "expected 4")

    matrix = [["0", "1"], ["1", "0"]]

    ans = s.maximalSquare(matrix)
    print(ans, "expected 1")

    matrix = [["0"]]

    ans = s.maximalSquare(matrix)
    print(ans, "expected 0")

    matrix = [
        ["1", "1", "1"],
        ["1", "1", "1"],
        ["1", "1", "1"],
    ]

    ans = s.maximalSquare(matrix)
    print(ans, "expected 9")

    matrix = [
        ["1", "1", "1", "1", "0"],
        ["1", "1", "1", "1", "0"],
        ["1", "1", "1", "1", "1"],
        ["1", "1", "1", "1", "1"],
        ["0", "0", "1", "1", "1"],
    ]

    ans = s.maximalSquare(matrix)
    print(ans, "expected 16")
