from typing import List


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        N = len(nums)

        if 0 <= N <= 2:
            nums.reverse()
            return

        for i in range(N - 1, 0, -1):
            a, b = i, i - 1

            if nums[a] > nums[b]:
                print(f"{nums[a]} > {nums[b]}")

                for c in range(N - 1, b - 1, -1):
                    if nums[c] > nums[b]:
                        break

                print(f"swaping {nums[b]} <-> {nums[c]}")

                nums[b], nums[c] = nums[c], nums[b]
                nums[b + 1 :] = nums[b + 1 :][::-1]

                break

        else:
            nums.reverse()


if __name__ == "__main__":
    # start = [1, 2, 3]
    #   |     [1, 3, 2]
    #   |     [2, 3, 1]
    #   |     [2, 1, 3]
    #   |     [3, 1, 2]
    # final = [3, 2, 1]

    cases = [
        ([1, 2, 3], [1, 3, 2]),
        ([3, 2, 1], [1, 2, 3]),
        ([1, 1, 5], [1, 5, 1]),
        ([1, 2], [2, 1]),
        ([1, 5, 1], [5, 1, 1]),
        ([5, 1, 1], [1, 1, 5]),
    ]
    s = Solution()

    for case, res in cases:
        print(f"case: {case}")
        s.nextPermutation(case)
        print(f"| {case} {'==' if case == res else '!='} {res} |", end="\n" * 2)
