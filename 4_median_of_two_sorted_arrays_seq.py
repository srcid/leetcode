from rich import print
from typing import List
from math import inf


def get(arr, idx, default=None):
    if 0 <= idx < len(arr):
        return arr[idx]
    return default

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        M, N = len(nums1), len(nums2)
        SIZE = M + N   # Size of arrays merged
        MID = SIZE // 2  # Middle index of the merged array
        i, j = 0, 0
        
        if N < M:
            nums1, nums2 = nums2, nums1
            M, N = N, M
        
        while i + j < (MID - 1 if SIZE % 2 == 0 else MID):
            if get(nums1, i, inf) <= get(nums2, j, -inf):
                i += 1
            else:
                j += 1

        if SIZE % 2 == 0:
            if get(nums1, i, inf) <= get(nums2, j, -inf):
                l = nums1[i]
                i += 1
            else:
                l = nums2[j]
                j += 1

            if 0 <= j < N:
                r = nums1[i] if get(nums1, i, inf) <= get(nums2, j, -inf) else nums2[j]
            else:
                r = nums1[i]

            return (l + r)/2
        else:
            return nums1[i] if get(nums1, i, inf) <= get(nums2, j, -inf) else nums2[j]


if __name__ == '__main__':
    sol = Solution()
    
    nums1, nums2 = [0,2,6], [0,7,16,17,19]
    print(sol.findMedianSortedArrays(nums1, nums2))
    
    nums1, nums2 = [100001], [100000]
    print(sol.findMedianSortedArrays(nums1, nums2))

