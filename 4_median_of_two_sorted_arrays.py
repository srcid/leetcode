from rich import print
from typing import List
from math import ceil, floor, inf


class Solution:
    @staticmethod
    def median(nums):
        mid = (len(nums) - 1) / 2
        l, r = floor(mid), ceil(mid)
        return (nums[l] + nums[r]) / 2

    @staticmethod
    def getitem(arr, idx, defaut):
        if 0 <= idx < len(arr):
            return arr[idx]
        else:
            return defaut

    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        M, N = len(nums1), len(nums2)
        TOTAL = M + N
        HALF = (TOTAL - 1) // 2

        if N < M:
            nums1, nums2 = nums2, nums1
            M, N = N, M

        if M == 0:
            return self.median(nums2)

        start, end = 0, M - 1

        while True:
            mid1 = (start + end) // 2
            mid2 = HALF - mid1 - 1

            print(f"{mid1=} {mid2=}")

            l1 = self.getitem(nums1, mid1, -inf)
            r1 = self.getitem(nums1, mid1 + 1, inf)
            l2 = self.getitem(nums2, mid2, -inf)
            r2 = self.getitem(nums2, mid2 + 1, inf)

            print(f"{l1=} {r1=} {l2=} {r2=}")

            if l1 <= r2 and l2 <= r1:
                if TOTAL % 2 == 0:
                    return (max(l1, l2) + min(r1, r2)) / 2

                return max(l1, l2)
            elif l1 > r2:
                end = mid1 - 1
            else:
                start = mid1 + 1


if __name__ == "__main__":
    sol = Solution()

    print("teste 1: ")
    nums1, nums2 = [0, 2, 6], [0, 7, 16, 17, 19]
    res = 6.5
    ans = sol.findMedianSortedArrays(nums1, nums2)
    print(ans, res, ans == res, end="\n\n")

    print("teste 2: ")
    nums1, nums2 = [100001], [100000]
    res = 100000.5
    ans = sol.findMedianSortedArrays(nums1, nums2)
    print(ans, res, ans == res, end="\n\n")

    print("teste 3: ")
    nums1, nums2 = [0, 2, 6, 7], [0, 7, 16, 17, 19]
    res = 7
    ans = sol.findMedianSortedArrays(nums1, nums2)
    print(ans, res, ans == res)
