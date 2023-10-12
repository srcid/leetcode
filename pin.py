# Problem description at
# https://www.codewars.com/kata/5263c6999e0f40dee200059d

from pprint import pprint
from itertools import product
from functools import partial
from operator import is_not

class Solution:
    def __init__(self):
        self.kb = (
            (  1, 2, 3  ),
            (  4, 5, 6  ),
            (  7, 8, 9  ),
            (None,0,None)
        )

        self.positions = {
            i * len(self.kb[0]) + j + 1 : (i, j)
            for i in range(3)
                for j in range(3)
        }

        self.positions[0] = (3,1)

    def pos(self, dig):
        return self.positions[dig]

    def psbls(self, i, j):
        return tuple(filter(partial(is_not, None), (
            self.kb[ i ][ j ]                                   ,
            self.kb[i-1][ j ] if i-1 >= 0              else None,
            self.kb[i+1][ j ] if i+1 < len(self.kb)    else None,
            self.kb[ i ][j-1] if j-1 >= 0              else None,
            self.kb[ i ][j+1] if j+1 < len(self.kb[0]) else None
        )))

    def solve(self, digits):
        return tuple(product(*(self.psbls(*self.pos(d)) for d in digits)))


digits = input()
s = Solution()
digits_arr = list(map(int,digits))
pprint([ ''.join(map(str, res)) for res in s.solve(digits_arr) ])
