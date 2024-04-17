from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix[0][0] <= target <= matrix[-1][-1]:
            return False

        for row in matrix:
            if row[0] <= target <= row[-1]:
                return target in row

        return False