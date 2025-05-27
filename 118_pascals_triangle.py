from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans = [[1]]

        while numRows > 1:
            numRows -= 1
            p = ans[-1]
            ans.append([1] + [p[i] + p[i + 1] for i in range(len(p) - 1)] + [1])

        return ans
