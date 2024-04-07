from dataclasses import dataclass

"""
This code is from claro henrique sales e carlos eduardo da silva ferreira.
"""

@dataclass
class Position:
  i: int
  j: int
  wasVisited: bool

class Solution:
  def isAdjacent(self, pos1, pos2):
    match abs(pos1.i - pos2.i), abs(pos1.j - pos2.j):
      case (0, 1) | (1, 0):
        return True
      case _:
        return False

  def solve_backward(self, prev_pos, left_word):
    if len(left_word) == 0:
      return self.solve_forward(self.save_middle, self.save_right)

    char = left_word[-1]
    adjs = (pos for pos in self.chars[char] if pos.wasVisited !=
            True and self.isAdjacent(pos, prev_pos))

    for adj_pos in adjs:
      adj_pos.wasVisited = True

      if self.solve_backward(adj_pos, left_word[:-1]):
        return True

      adj_pos.wasVisited = False

    return False

  def solve_forward(self, prev_pos: Position, right_word: str):
    if len(right_word) == 0:
      return True

    char = right_word[0]
    adjs = (pos for pos in self.chars[char] if pos.wasVisited !=
            True and self.isAdjacent(pos, prev_pos))

    for adj_pos in adjs:
      adj_pos.wasVisited = True

      if self.solve_forward(adj_pos, right_word[1:]):
        return True

      adj_pos.wasVisited = False

    return False

  def solve_aux(self, prev_pos, left_word, right_word):
    self.save_right = right_word
    self.save_middle = prev_pos
    return self.solve_backward(prev_pos, left_word)

  def solve(self, word):
    least_often_char, least_often_char_pos = min(
        self.chars.items(), key=lambda item: len(item[1]))
    least_often_char_idx = word.find(least_often_char)

    for pos in least_often_char_pos:
      pos.wasVisited = True
      if self.solve_aux(pos, word[:least_often_char_idx], word[least_often_char_idx+1:]):
        return True
      pos.wasVisited = False

    return False

  def exist(self, board, word):
    self.board = board
    self.M = len(board)
    self.N = len(board[0])
    self.chars = {char: [] for char in word}

    if len(word) > self.M * self.N:
      return False

    for i in range(len(board)):
      for j in range(len(board[0])):
        if (char := board[i][j]) in self.chars:
          self.chars[char].append(Position(i, j, False))

    return self.solve(word)


s = Solution()

l0 = [["A", "A", "A", "A", "A", "A"],
      ["A", "A", "A", "A", "A", "A"],
      ["A", "A", "A", "A", "A", "A"],
      ["A", "A", "A", "A", "A", "A"],
      ["A", "A", "A", "A", "A", "A"],
      ["A", "A", "A", "A", "A", "B"]]
w0 = "AAAAAAAAAAAAAAB"
l1 = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
w1 = "ABCCED"
l2 = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
w2 = "SEE"
l3 = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
w3 = "ABCB"
l4 = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
w4 = "CSA"
l5 = [["A", "A", "A", "A", "A", "A"],
      ["A", "A", "A", "A", "A", "A"],
      ["A", "A", "A", "A", "A", "A"],
      ["A", "A", "A", "A", "A", "A"],
      ["A", "A", "A", "A", "A", "A"],
      ["A", "A", "A", "A", "A", "A"]]
w5 = "AAAAAAAAAAAAAAB"
l6 = [["A", "B", "C", "E"],
      ["S", "F", "C", "S"],
      ["A", "D", "E", "E"]]
w6 = "ABCB"
l7 = [["A", "Z", "A", "A"],
      ["A", "B", "B", "B"],
      ["A", "C", "B", "B"],
      ["A", "B", "B", "B"],
      ["A", "B", "B", "B"]]
w7 = ''.join(reversed("BBBBBBBCBZ"))
l9 = [["A", "Z", "X"],
      ["X", "X", "A"]]
w9 = "AZA"

print(s.exist(l0, w0), 'True')
print(s.exist(l1, w1), 'True')
print(s.exist(l2, w2), 'True')
print(s.exist(l3, w3), 'False')
print(s.exist(l4, w4), 'False')
print(s.exist(l5, w5), 'False')
print(s.exist(l6, w6), 'False')
print(s.exist(l9, w9), 'False')
print(s.exist(l7, w7), 'True')
