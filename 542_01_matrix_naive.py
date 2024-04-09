"""WARNING: This solution doesn't pass on leetcode: timeout"""

from typing import List
from dataclasses import dataclass
from rich import print

@dataclass
class Position:
    i: int
    j: int

    def distance(self, p):
        return sum(map(abs, vars(self - p).values()))
    
    def abs_greater(self):
        return max(map(abs, vars(self).values()))
    
    def distance_real(self, p):
        return (self - p).abs_greater()

    def is_in_diagonal(self, p):
        return len(set(map(abs, vars(self - p).values()))) == 1
    
    def is_in_row_or_col(self, p):
        return 0 in vars(self - p).values()
    
    def _with(self, **kwargs):
        return Position(
            kwargs.get('x') or self.i, 
            kwargs.get('y') or self.j
        )

    def __sub__(self, p):
        return Position(self.i - p.i, self.j - p.j)

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        M = len(mat)
        N = len(mat[0])

        zeros = []
        positions = []

        for i in range(M):
            for j in range(N):
                p = Position(i, j)
                if mat[i][j] == 0:
                    zeros.append(p)
                else:
                    positions.append(p)

        for p in positions:
            mat[p.i][p.j] = min(map(p.distance, zeros))

        return mat

if __name__ == '__main__':
    sol = Solution()
    mat = [
        [1,0,1,1,0,0,1,0,0,1],
        [0,1,1,0,1,0,1,0,1,1],
        [0,0,1,0,1,0,0,1,0,0],
        [1,0,1,0,1,1,1,1,1,1],
        [0,1,0,1,1,0,0,0,0,1],
        [0,0,1,0,1,1,1,0,1,0],
        [0,1,0,1,0,1,0,0,1,1],
        [1,0,0,0,1,1,1,1,0,1],
        [1,1,1,1,1,1,1,0,1,0],
        [1,1,1,1,0,1,0,0,1,1]
    ]
    res = [
        [1,0,1,1,0,0,1,0,0,1],
        [0,1,1,0,1,0,1,0,1,1],
        [0,0,1,0,1,0,0,1,0,0],
        [1,0,1,0,1,1,1,1,1,1],
        [0,1,0,1,1,0,0,0,0,1],
        [0,0,1,0,1,1,1,0,1,0],
        [0,1,0,1,0,1,0,0,1,1],
        [1,0,0,0,1,2,1,1,0,1],
        [2,1,1,1,1,2,1,0,1,0],
        [3,2,2,1,0,1,0,0,1,1]
    ]

    mat2 = [
        [0,0,1,0,1,1,1,0,1,1],
        [1,1,1,1,0,1,1,1,1,1],
        [1,1,1,1,1,0,0,0,1,1],
        [1,0,1,0,1,1,1,0,1,1],
        [0,0,1,1,1,0,1,1,1,1],
        [1,0,1,1,1,1,1,1,1,1],
        [1,1,1,1,0,1,0,1,0,1],
        [0,1,0,0,0,1,0,0,1,1],
        [1,1,1,0,1,1,0,1,0,1],
        [1,0,1,1,1,0,1,1,1,0]
    ]
    res2 = [
        [0,0,1,0,1,2,1,0,1,2],
        [1,1,2,1,0,1,1,1,2,3],
        [2,1,2,1,1,0,0,0,1,2],
        [1,0,1,0,1,1,1,0,1,2],
        [0,0,1,1,1,0,1,1,2,3],
        [1,0,1,2,1,1,1,2,1,2],
        [1,1,1,1,0,1,0,1,0,1],
        [0,1,0,0,0,1,0,0,1,2],
        [1,1,1,0,1,1,0,1,0,1],
        [1,0,1,1,1,0,1,2,1,0]
    ]

    mat3 = [
        [0,0,0],
        [0,1,0],
        [1,1,1]
    ]

    res3 = [
        [0,0,0],
        [0,1,0],
        [1,2,1]
    ]

    mat4= [
        [1,0,1,1],
        [1,1,1,1],
        [0,0,1,1],
        [1,0,1,1]
    ]
    res4 = [
        [1,0,1,2],
        [1,1,2,3],
        [0,0,1,2],
        [1,0,1,2]
    ]

    print(sol.updateMatrix(mat4) == res4)
    print(sol.updateMatrix(mat3) == res3)
    print(sol.updateMatrix(mat) == res)
    print(sol.updateMatrix(mat2) == res2)