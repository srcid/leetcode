from typing import List, Dict
from pydantic import validate_arguments
from collections import namedtuple

Position = namedtuple('Position', ['i','j'])

class Solution:
    @validate_arguments
    def isAdjacent(self, pos1: Position, pos2: Position) -> bool:
        match abs(pos1.i - pos2.i), abs(pos1.j - pos2.j):
            case (0, 1) | (1, 0):
                return True
            case _:
                return False
        
    @validate_arguments
    def solve_aux(self, word: str, visited: List[Position]) -> bool:
        if len(word) == 0:
            return True
        
        prev_pos = visited[-1]
        char = word[0]
        adjs = (pos for pos in self.chars[char] if self.isAdjacent(prev_pos, pos) and pos not in visited)

        return any((self.solve_aux(word[1:], visited+[adj_pos]) for adj_pos in adjs))

    @validate_arguments
    def solve(self, word: str):
        if any(len(self.chars[char]) == 0 for char in self.chars):
            return False

        char = word[0]
        return any((self.solve_aux(word[1:], [pos]) for pos in self.chars[char]))

    @validate_arguments
    def exist(self, board: List[List[str]], word: str) -> bool:        
        self.board = board
        self.M = len(board)
        self.N = len(board[0])
        self.chars = { char: [] for char in word }

        if len(word) > self.M * self.N:
            return False

        for i in range(len(board)):
            for j in range(len(board[0])):
                if (char := board[i][j]) in self.chars:
                    self.chars[char].append(Position(i,j))
        
        return self.solve(word)

s = Solution()

l0 = [["A","A","A","A","A","A"],
      ["A","A","A","A","A","A"],
      ["A","A","A","A","A","A"],
      ["A","A","A","A","A","A"],
      ["A","A","A","A","A","A"],
      ["A","A","A","A","A","B"]]
w0 = "AAAAAAAAAAAAAAB"
l1 = [["A","B","C","E"],
      ["S","F","C","S"],
      ["A","D","E","E"]]
w1 = "ABCCED"
l2 = [["A","B","C","E"],
      ["S","F","C","S"],
      ["A","D","E","E"]]
w2 = "SEE"
l3 = [["A","B","C","E"],
      ["S","F","C","S"],
      ["A","D","E","E"]]
w3 = "ABCB"
l4 = [["A","B","C","E"],
      ["S","F","C","S"],
      ["A","D","E","E"]]
w4 = "CSA"
l5 = [["A","A","A","A","A","A"],
      ["A","A","A","A","A","A"],
      ["A","A","A","A","A","A"],
      ["A","A","A","A","A","A"],
      ["A","A","A","A","A","A"],
      ["A","A","A","A","A","A"]]
w5 = "AAAAAAAAAAAAAAB"
l6 = [["A","B","C","E"],
      ["S","F","C","S"],
      ["A","D","E","E"]]
w6 = "ABCB"
l7 = [["A","Z","A","A"],
      ["A","B","B","B"],
      ["A","C","B","B"],
      ["A","B","B","B"],
      ["A","B","B","B"]]
w7 = "BBBBBBBCBZ"
l8 = [["A","Z"]]
w8 = "AZA"
l9 = [["A", "Z", "X"],
      ["X", "X", "A"]]
w9 = "AZA"
l10 = [["A", "Z", "X", "X", "X", "X"]]
w10 = "AZA"


print(s.exist(l0, w0), 'True')
print(s.exist(l1, w1), 'True')
print(s.exist(l2, w2), 'True')
print(s.exist(l3, w3), 'False')
print(s.exist(l4, w4), 'False')
print(s.exist(l5, w5), 'False')
print(s.exist(l6, w6), 'False')
print(s.exist(l7, w7), 'True')
print(s.exist(l8, w8), 'False')
print(s.exist(l9, w9), 'False')
print(s.exist(l10, w10), 'False')
