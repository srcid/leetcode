from typing import List
from queue import SimpleQueue


class Solution:
    def isv(self, pos):
        i, j = pos
        return (0 <= i < self.M and 0 <= j < self.N and self.grid[i][j])

    def adjs(self, pos):
        i, j = pos
        return filter(self.isv,(
            (i+1, j),
            (i-1, j),
            (i, j+1), 
            (i, j-1)
        ))

    def bfs(self, pos):
        nf = 0
        i, j = pos
        nf += self.grid[i][j]
        self.grid[i][j] = None

        q = SimpleQueue()
        q.put((i, j))

        while not q.empty():
            i, j = q.get()
            for x, y in self.adjs((i,j)):
                nf += self.grid[x][y]
                self.grid[x][y] = None
                q.put((x,y))

        return nf

    def findMaxFish(self, grid: List[List[int]]) -> int:
        self.grid = grid
        self.M = len(self.grid)
        self.N = len(self.grid[0])
        fishes = 0

        for i in range(self.M):
            for j in range(self.N):
                if self.grid[i][j]:
                    nf = self.bfs((i,j))
                    if nf > fishes:
                        fishes = nf
                else:
                    self.grid[i][j] = None    

        return fishes

if __name__ == '__main__':
    sol = Solution()
    grid = [[8, 6], [2, 6]]

    print(sol.findMaxFish(grid))
