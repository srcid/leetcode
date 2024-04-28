from collections import deque
from typing import List

from rich import print


class Solution:
    def isv(self, p):
        i, j = p
        return 0 <= i < self.M and 0 <= j < self.N

    def adjs(self, p):
        i, j = p
        return filter(self.isv, ((i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)))

    def adjsv(self, p):
        return (self.isInfected[x][y] for x, y in self.adjs(p))

    def spread(self):
        """Spread the virus through the board"""
        toSpread = []

        for i in range(self.M):
            for j in range(self.N):
                if self.isInfected[i][j] == 0 and 1 in self.adjsv((i, j)):
                    toSpread.append((i, j))

        for i, j in toSpread:
            self.isInfected[i][j] = 1

    def setWallsOnBlock(self, p):
        """Set walls into a block of virtus and return the number of walls was set down"""
        q = deque([p])
        ans = 0

        while len(q):
            i, j = q.pop()

            match self.isInfected[i][j]:
                case 1:
                    """In this case we're adding repeating positions to the queue, but
                    it's correct, because we can put more than one wall on a single
                    cell. Actually, we can put even 4 walls on a cell.
                    """
                    self.isInfected[i][j] = -1
                    q.extend(self.adjs((i, j)))
                case 0:
                    ans += 1

        return ans

    def damage(self, p):
        """return the damage of a block of virus can cause and convert all virus
        positions to none
        """
        q = deque([p])
        demangedpos = set()

        while len(q):
            i, j = q.popleft()

            match self.isInfected[i][j]:
                case 0:
                    demangedpos.add((i, j))
                case 1:
                    self.isInfected[i][j] = None
                    q.extend(self.adjs((i, j)))

        return (p, len(demangedpos))

    def mostDamangedBlocks(self):
        damaged_blocks = []
        for i in range(self.M):
            for j in range(self.N):
                if self.isInfected[i][j] == 1:
                    d = self.damage((i, j))
                    damaged_blocks.append(d)

        for i in range(self.M):
            for j in range(self.N):
                if self.isInfected[i][j] == None:
                    self.isInfected[i][j] = 1

        return max(damaged_blocks, default=(None, None), key=lambda x: x[1])[0]

    def containVirus(self, isInfected: List[List[int]]) -> int:
        self.isInfected = isInfected
        self.M = len(self.isInfected)
        self.N = len(self.isInfected[0])
        ans = 0

        while True:
            pos = self.mostDamangedBlocks()

            if pos == None:
                break

            nwalls = self.setWallsOnBlock(pos)

            if nwalls == 0:
                break

            ans += nwalls

            self.spread()

        return ans


if __name__ == "__main__":
    m1 = [
        [0, 1, 0, 0, 0, 0, 0, 1],
        [0, 1, 0, 0, 0, 0, 0, 1],
        [0, 0, 0, 0, 0, 0, 0, 1],
        [0, 0, 0, 0, 0, 0, 0, 0],
    ]
    m2 = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
    m3 = [
        [1, 1, 1, 0, 0, 0, 0, 0, 0],
        [1, 0, 1, 0, 1, 1, 1, 1, 1],
        [1, 1, 1, 0, 0, 0, 0, 0, 0],
    ]
    m4 = [[0]]
    m5 = [
        [0, 1, 0, 1, 1, 1, 1, 1, 1, 0],
        [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 1, 1, 0, 0, 0, 1, 0],
        [0, 0, 0, 1, 1, 0, 0, 1, 1, 0],
        [0, 1, 0, 0, 1, 0, 1, 1, 0, 1],
        [0, 0, 0, 1, 0, 1, 0, 1, 1, 1],
        [0, 1, 0, 0, 1, 0, 0, 1, 1, 0],
        [0, 1, 0, 1, 0, 0, 0, 1, 1, 0],
        [0, 1, 1, 0, 0, 1, 1, 0, 0, 1],
        [1, 0, 1, 1, 0, 1, 0, 1, 0, 1],
    ]
    s = Solution()
    print(s.containVirus(m1), 10)
    print(s.containVirus(m2), 4)
    print(s.containVirus(m3), 13)
    print(s.containVirus(m4), 0)
    print(s.containVirus(m5), 38)
