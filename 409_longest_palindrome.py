from collections import Counter


class Solution:
    def longestPalindrome(self, s: str) -> int:
        ans = len(s)
        c = Counter(s)

        while True:
            n = ans // 2

            acc = sum(map(lambda x: x // 2, c.values()))

            if acc == n:
                break

            ans -= 1

        return ans


class Solution2:
    def longestPalindrome(self, s: str) -> int:
        ans = 0
        c = Counter(s)

        for ch, val in c.items():
            if val >= 2:
                if val % 2:
                    ans += val - 1
                    c[ch] = 1
                else:
                    ans += val

        if 1 in c.values():
            ans += 1

        return ans
