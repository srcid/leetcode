from typing import List

class Solution:
    def jooj(self, i: int, j: int) -> None:
        if not (0 <= i < self.M) or not (0 <= j < self.N) or self.board[i][j] == '.':
            return

        self.board[i][j] = '.'
        right = self.jooj(i, j+1)
        down = self.jooj(i+1, j)

        

    def countBattleships(self, board: List[List[str]]) -> int:
        self.board = board
        self.M = len(board)
        self.N = len(board[0])
        nboats = 0

        for i in range(self.M):
            for j in range(self.N):
                if self.board[i][j] == 'X':
                    self.jooj(i, j)
                    nboats += 1
        
        return nboats

s = Solution()
board = [["X",".",".","X"],
         [".",".",".","X"],
         [".",".",".","X"]]

print(s.countBattleships(board))