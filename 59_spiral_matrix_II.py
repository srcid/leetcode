from typing import List
from pprint import pprint

class Solution:
    def __init__(self) -> None:
        self.getVal = self.__getVal()

    def __getVal(self):
        val = 1

        while True:
            yield val
            val += 1

    def generate_aux(self, i, j):
        if i > j:
            return

        # ceil row
        for q in range(i, j):
            self.matrix[i][q] = next(self.getVal)

        # rightest column
        for p in range(i+1, j-1):
            self.matrix[p][j-1] = next(self.getVal)

        # floor row
        for q in range(j - 1, i, -1):
            self.matrix[j-1][q] = next(self.getVal)

        # leftest column
        for p in range(j - 1, i, -1):
            self.matrix[p][i] = next(self.getVal)

        self.generate_aux(i+1, j-1)

    def generateMatrix(self, n: int) -> List[List[int]]:
        self.matrix = [ [0]*n for _ in range(n) ]
        self.N = n
        self.val = 0

        self.generate_aux(0, self.N)

        return self.matrix
    
s = Solution()

pprint(s.generateMatrix(6))
