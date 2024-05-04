from itertools import chain
from typing import List


class Solution:
    def isValidRow(self, row):
        elements = tuple(filter(lambda e: e != ".", row))
        setelements = set(elements)

        return setelements <= {str(i) for i in range(1, 10)} and len(
            setelements
        ) == len(elements)

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = len(board)
        cols = len(board[0])

        for row in board:
            if not self.isValidRow(row):
                return False

        for j in range(cols):
            col = chain(*[row[j : j + 1] for row in board])
            if not self.isValidRow(col):
                return False

        for i in range(0, rows, 3):
            for j in range(0, cols, 3):
                sub = chain(*[row[j : j + 3] for row in board[i : i + 3]])
                if not self.isValidRow(sub):
                    return False

        return True
