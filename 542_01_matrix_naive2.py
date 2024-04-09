"""WARNING: This solution doesn't pass on leetcode: timeout"""

from typing import List
from rich.pretty import pprint
from dataclasses import dataclass
from math import inf
    
class Solution:
    def isInBounds(self, pos):
        i, j = pos
        return (0 <= i < self.M and 0 <= j < self.N)

    def adjs(self, pos):
        i, j = pos
        return filter(
            self.isInBounds, (
                (i+1, j  ),
                (i-1, j  ),
                (i  , j+1),
                (i  , j-1)
            )
        )
    
    def distance(self, pos):
        i, j = pos
        if self.positions[pos]:
            return self.mat[i][j]
        
        self.positions[pos] = True
        
        self.mat[i][j] = 1 + min(map(self.distance, self.adjs(pos)))
        
        self.positions[pos] = False
        
        return self.mat[i][j]

    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        self.mat = mat
        self.M = len(mat)
        self.N = len(mat[0])
        self.positions = {}

        for i in range(self.M):
            for j in range(self.N):
                if self.mat[i][j]:
                    self.positions[i,j] = False
                else:
                    self.positions[i,j] = True

        for pos in list(filter(self.positions.get, self.positions)):
            adjs = self.adjs(pos)
                
            for adj in adjs:
                if not self.positions[adj]:
                    self.positions[adj] = True

        for pos in self.positions:
            if not self.positions[pos]:
                self.distance(pos)

        return self.mat

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

    pprint(sol.updateMatrix(mat4) == res4)
    pprint(sol.updateMatrix(mat3) == res3)
    pprint(sol.updateMatrix(mat) == res)
    pprint(sol.updateMatrix(mat2) == res2)