from functools import cache
from typing import List


class Solution:
    @cache
    def ispal(self, s: str) -> bool:
        N = len(s)
        return s[: N // 2] == s[: (N - 1) // 2 : -1]

    def dfs(self, start, path):
        if start == self.N:
            self.ans.append(path)
            return

        for i in range(start, self.N):
            if self.ispal(self.s[start : i + 1]):
                self.dfs(i + 1, path + [self.s[start : i + 1]])

    def partition(self, s: str) -> List[List[str]]:
        self.ans = []
        self.N = len(s)
        self.s = s
        self.dfs(0, [])
        return self.ans


if __name__ == "__main__":
    cases = ["a", "aab", "carlos", "aibohphobia"]

    s = Solution()

    for case in cases:
        ans = s.partition(case)
        print("-> ", case, ans)
