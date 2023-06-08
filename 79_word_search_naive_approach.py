from typing import List, Dict
from pydantic import validate_arguments

class Solution:
    """
    In this approach, we iterate through the matrix until we find a char that march the
    word first char then we look out all its adjacent cell, recursively, trying to find 
    the test of the word.
    """
    def solve(self, i: int, j: int, word: str) -> bool:
        if word == '':
            return True
        
        if i < 0 or i >= len(self.board):
            return False
        
        if j < 0 or j >= len(self.board[0]):
            return False
        
        l = self.board[i][j]

        if l != word[0]:
            return False
        
        self.board[i][j] = None

        res = any((self.solve(i+1, j, word[1:]), self.solve(i-1, j, word[1:]),
            self.solve(i, j+1, word[1:]), self.solve(i, j-1, word[1:])))
            
        self.board[i][j] = l
        
        return res

    @validate_arguments
    def exist(self, board: List[List[str]], word: str) -> bool:
        self.board = board
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0] and self.solve(i, j, word):
                    return True
        
        return False
        

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
