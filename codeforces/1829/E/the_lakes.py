from typing import List
from dataclasses import dataclass

@dataclass
class Position:
    i: int
    j: int
    visited: bool = False

class Solution:
    def isAdj(self, pos1: Position, pos2: Position) -> bool:
        return (abs(pos1.i - pos2.i), abs(pos1.j - pos2.j)) in ((1, 0), (0, 1))

    def findLake(self) -> int:
        self.pos_with_water[0].visited = True
        q = [ self.pos_with_water[0] ]                
        vol = 0
        
        while len(q) > 0:
            cur_pos = q.pop()
            vol += self.matrix[cur_pos.i][cur_pos.j]
            
            for pos in filter(lambda pos: pos.visited == False and self.isAdj(pos, cur_pos), self.pos_with_water):
                pos.visited = True
                q.append(pos)
            
        return vol

    def volOfMaxLake(self, matrix: List[List[int]]) -> int:
        self.M, self.N = len(matrix), len(matrix[0])
        self.matrix = matrix
        self.pos_with_water: List[Position] = []
        ans = [0]

        for i in range(self.M):
            for j in range(self.N):
                if self.matrix[i][j] != 0:
                    self.pos_with_water.append(Position(i, j))

        while len(self.pos_with_water) > 0:
            ans.append(self.findLake())
            self.pos_with_water = list(filter(lambda pos: pos.visited == False, self.pos_with_water))
        
        return max(ans)

ncases = int(input())
ans = []

for _ in range(ncases):
    s = Solution()
    m, n = list(map(int, input().split(' ')))
    matrix = []

    for i in range(m):
        matrix.append(list(map(int, input().split(' '))))

    maxvol = s.volOfMaxLake(matrix)
    ans.append(maxvol)

for vol in ans:
    print(vol)
