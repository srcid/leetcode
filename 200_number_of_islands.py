from typing import List
from queue import SimpleQueue


class Solution:
    def isv(self, point):
        i, j = point
        return (0 <= i < self.M and 0 <= j < self.N)

    def adjs(self, i, j):
        return filter(self.isv, ((i,j+1),(i,j-1),(i+1,j),(i-1,j)))

    def bfs(self, i, j):
        q = SimpleQueue()
        self.grid[i][j] = None
        q.put((i,j))

        while not q.empty():
            i, j = q.get()
            
            for x, y in self.adjs(i, j):
                if self.grid[x][y] not in ("0", None):
                    self.grid[x][y] = None
                    q.put((x, y))
        
        return 1


    def numIslands(self, grid: List[List[str]]) -> int:
        self.M = len(grid)
        self.N = len(grid[0])
        self.grid = grid
        islands = 0

        for i in range(self.M):
            for j in range(self.N):
                if self.grid[i][j] == "1":
                    islands += self.bfs(i,j)

        return islands