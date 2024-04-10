from rich import print
from typing import List
from math import inf


class Solution:
    def median(nums):
        mid = len(nums) // 2
        
        if len(nums) % 2:
            return (nums[mid] + nums[mid+1]) / 2
        
        return nums[mid]

    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        M, N = len(nums1), len(nums2)
        MERGED_SIZE = M + N  # Size of arrays merged
        MERGED_HALF = MERGED_SIZE // 2
        
        if N < M:
            nums1, nums2 = nums2, nums1
            M, N = N, M

        if M == 0:
            return self.median(nums2)
        
        l, r = 0, M - 1

        while True:
            i = (l+r) // 2
            j = MERGED_HALF - i - 2

            nums1Left  = nums1[i]   if i >= 0    else -inf
            nums1Right = nums1[i+1] if (i+1) < M else inf
            nums2left  = nums2[j]   if j >= 0    else -inf
            nums2Right = nums2[j+1] if (j+1)     else inf

            # Partition is correct
            if nums1Left <= nums2Right and nums2left <= nums1Right:
                # Odd
                if MERGED_SIZE % 2:
                    return min(nums1Right, nums2Right)
                # Even
                else:
                    return (max(nums1Left, nums2left) + min(nums1Right, nums2Right)) / 2
            elif nums1Left > nums2Right:
                r = i - 1
            else:
                l = i + 1

if __name__ == '__main__':
    sol = Solution()
    
    # nums1, nums2 = [0,2,6], [0,7,16,17,19]
    # print(sol.findMedianSortedArrays(nums1, nums2))
    
    nums1, nums2 = [100001], [100000]
    print(sol.findMedianSortedArrays(nums1, nums2))
