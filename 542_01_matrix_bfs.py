from rich.pretty import pprint
from typing import List
from queue import Queue
from itertools import filterfalse


class Solution:
    def inBounds(self, pos):
        i, j = pos
        return (0 <= i < self.M and 0 <= j < self.N)
    
    def adjs(self, pos):
        i, j = pos
        return filter(
            self.inBounds,
            (
                (i+1, j  ),
                (i-1, j  ),
                (i  , j+1),
                (i  , j-1)
            )
        )

    def wasVisited(self, pos):
        i, j = pos
        return self.mat[i][j] != -1

    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        self.M = len(mat)
        self.N = len(mat[0])
        self.mat = mat
        visited = Queue()

        for i in range(self.M):
            for j in range(self.N):
                if self.mat[i][j]:
                    self.mat[i][j] = -1
                else:
                    visited.put((i, j))

        while not visited.empty():
            pos = visited.get()
            i, j = pos

            for adj in filterfalse(self.wasVisited,self.adjs(pos)):
                k, l = adj
                self.mat[k][l] = mat[i][j] + 1
                visited.put(adj)

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