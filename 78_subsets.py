from itertools import combinations
from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        N = len(nums)
        ans = [[]]

        for i in range(1, N + 1):
            ans.extend(combinations(nums, i))

        return ans
