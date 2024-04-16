from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        M = len(matrix)
        N = len(matrix[0])

        if not matrix[0][0] <= target <= matrix[M-1][N-1]:
            return False

        for row in matrix:
            if row[0] <= target <= row[-1]:
                return target in row

        return False