from collections import defaultdict
from functools import partial
from operator import contains
from typing import List


def flip(func):
    def inner(*args):
        return func(*args[::-1])

    return inner


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        M = len(board)
        N = len(board[0])

        row = defaultdict(set)
        col = defaultdict(set)
        grd = defaultdict(set)

        for i in range(M):
            for j in range(N):
                val = board[i][j]

                if val != ".":
                    containsVal = partial(flip(contains), val)

                    if any(map(containsVal, (row[i], col[j], grd[i // 3, j // 3]))):
                        return False

                    row[i].add(val)
                    col[j].add(val)
                    grd[i // 3, j // 3].add(val)
                    # It could be an index k = i // 3 * 3 + j // 3

        return True


if __name__ == "__main__":
    board = [
        ["5", "3", ".", ".", "7", ".", ".", ".", "."],
        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"],
    ]
    s = Solution()

    print(s.isValidSudoku(board))
