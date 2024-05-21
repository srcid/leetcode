from operator import xor
from functools import reduce
from itertools import combinations
from typing import List


class Solution:
    def subsetXor(self, nums):
        return reduce(xor, nums, 0)

    def subsetXORSum(self, nums: List[int]) -> int:
        N = len(nums)
        acc = 0

        for i in range(1, N + 1):
            for cmb in combinations(nums, i):
                acc += self.subsetXor(cmb)

        return acc
