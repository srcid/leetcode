from itertools import batched
from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        i, e = 0, len(nums) - 1

        while e >= i:
            m = (i + e) // 2
            
            if nums[m] < target:
                i = m + 1
            elif nums[m] > target:
                e = m - 1
            else:
                f, l = m, m

                while f >= 0 and nums[f] == target:
                    f -= 1
                while l < len(nums) and nums[l] == target:
                    l += 1

                return [f + 1, l - 1]

        return [-1, -1]


if __name__ == "__main__":
    inputs = [[5, 7, 7, 8, 8, 10], 8, [5, 7, 7, 8, 8, 10], 6, [], 0]

    s = Solution()

    for nums, t in batched(inputs, 2):
        print(nums, t)
        print(s.searchRange(nums, t))
