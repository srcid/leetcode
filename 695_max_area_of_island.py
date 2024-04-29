from itertools import chain
from typing import List


class Solution:
    def isv(self, pos):
        i, j = pos
        return 0 <= i < self.rows and 0 <= j < self.cols

    def adjs(self, pos):
        i, j = pos
        return filter(self.isv, ((i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)))

    def dfs(self, pos):
        s = [pos]
        area = 0

        while len(s):
            i, j = s.pop()
            if self.grid[i][j] == 1:
                self.grid[i][j] = None
                s.extend(self.adjs((i, j)))
                area += 1

        return area

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        self.grid = grid
        self.rows = len(grid)
        self.cols = len(grid[0])
        max_area = 0

        for idx, e in enumerate(chain(*grid)):
            if e == 1:
                area = self.dfs(divmod(idx, self.cols))
                if area > max_area:
                    max_area = area

        return max_area
