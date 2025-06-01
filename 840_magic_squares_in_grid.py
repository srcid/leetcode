from itertools import chain
from typing import List


def mirror(matrix):
    mirrored = [row[::-1] for row in matrix]
    return mirrored


def diagonal(matrix):
    diag = [matrix[i][i] for i in range(len(matrix))]
    return diag


def transpose(matrix):
    transposed = [[row[j] for row in matrix] for j in range(len(matrix[0]))]
    return transposed


def is_valid(matrix):
    nums = set(chain(*matrix))

    return len({1, 2, 3, 4, 5, 6, 7, 8, 9} - nums) == 0


def isMagic(matrix, i, j):
    submatrix = [subrow[j : j + 3] for subrow in matrix[i : i + 3]]

    if not is_valid(submatrix):
        return False

    r = [sum(row) for row in submatrix]
    c = [sum(row) for row in transpose(submatrix)]
    d = [sum(diagonal(submatrix)), sum(diagonal(mirror(submatrix)))]

    first, *rcd = chain(r, c, d)

    return all((first == value for value in rcd))


class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        M, N = len(grid), len(grid[0])

        if M < 3 or N < 3:
            return 0

        cnt = 0

        for i in range(M - 2):
            for j in range(N - 2):
                if isMagic(grid, i, j):
                    cnt += 1

        return cnt


if __name__ == "__main__":
    grids = [
        (
            [
                [4, 3, 8, 4],
                [9, 5, 1, 9],
                [2, 7, 6, 2],
            ],
            1,
        ),
        # too small
        ([[8]], 0),
        # same sum, but equal numbers
        (
            [
                [5, 5, 5],
                [5, 5, 5],
                [5, 5, 5],
            ],
            0,
        ),
        (
            [
                [2, 7, 6, 9],
                [9, 5, 1, 6],
                [4, 3, 8, 8],
                [1, 4, 10, 1],
            ],
            1,
        ),
    ]
    s = Solution()

    for grid, expected in grids:
        ans = s.numMagicSquaresInside(grid)
        print(f"{ans=}, {expected=}")
