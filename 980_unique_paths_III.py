from collections import deque
from enum import IntEnum
from functools import partial, wraps
from itertools import chain
from operator import contains, countOf, indexOf
from typing import List


def flip(func):
    @wraps(func)
    def newfunc(*args):
        return func(*args[::-1])

    return newfunc


class PosType(IntEnum):
    blocked = -1
    available = 0
    starting = 1
    ending = 2


class Solution:
    def isv(self, p):
        i, j = p
        return (
            0 <= i < self.M
            and 0 <= j < self.N
            and self.grid[i][j] not in (PosType.blocked, PosType.starting)
        )

    def adjs(self, p):
        i, j = p
        return filter(self.isv, ((i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)))

    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        self.grid = grid
        self.M = len(grid)
        self.N = len(grid[0])

        # one dim of grid is 1
        if 1 in (self.M, self.N):
            containsBlocked = partial(flip(contains), PosType.blocked)
            # the first cell must be the starting(1), otherwise it can passes to all
            # cells; and cannot have a block(-1) in its path
            return (
                1
                if self.grid[0][0] == PosType.starting
                and not any(map(containsBlocked, (self.grid[0], chain(*self.grid))))
                else 0
            )

        availableCounter = countOf(chain(*self.grid), PosType.available)
        initial = divmod(indexOf(chain(*self.grid), PosType.starting), self.N)
        s = deque([(*pos, set()) for pos in self.adjs(initial)])
        ans = 0

        while len(s):
            i, j, visited = s.pop()

            if self.grid[i][j] == PosType.ending and len(visited) == availableCounter:
                ans += 1
            else:
                visited.add((i, j))
                s.extend(
                    (*pos, visited.copy())
                    for pos in self.adjs((i, j))
                    if pos not in visited
                )

        return ans


if __name__ == "__main__":
    grid1, r1 = [[1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 2, -1]], 2
    grid2, r2 = [[1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 2]], 4
    grid3, r3 = [[0, 1], [2, 0]], 0
    grid4, r4 = [[1, 0, 0, 2]], 1
    grid5, r5 = [[1], [0], [0], [2]], 1
    grid6, r6 = [[1, 0, -1, 2]], 0
    grid7, r7 = [[1], [0], [-1], [2]], 0
    grid8, r8 = [[0], [1], [0], [2]], 0
    grid9, r9 = [[0, 0, 0, 0, 0, 0, 2, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 1, 0]], 1
    grid10, r10 = [[1, 2]], 1

    s = Solution()

    print(f"{s.uniquePathsIII(grid1) = } {r1 = }")
    print(f"{s.uniquePathsIII(grid2) = } {r2 = }")
    print(f"{s.uniquePathsIII(grid3) = } {r3 = }")
    print(f"{s.uniquePathsIII(grid4) = } {r4 = }")
    print(f"{s.uniquePathsIII(grid5) = } {r5 = }")
    print(f"{s.uniquePathsIII(grid6) = } {r6 = }")
    print(f"{s.uniquePathsIII(grid7) = } {r7 = }")
    print(f"{s.uniquePathsIII(grid8) = } {r8 = }")
    print(f"{s.uniquePathsIII(grid9) = } {r9 = }")
    print(f"{s.uniquePathsIII(grid10) = } {r10 = }")
