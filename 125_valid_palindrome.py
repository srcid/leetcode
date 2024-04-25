"""
With this approach we include the middle element in the comparison

N = len(s)
s[: (N - 1) // 2 + 1] == s[N // 2 :][::-1]

case N is odd
('a', 'm', 'a', 'n', 'a', 'p', 'l', 'a', 'n', 'a', 'c')
('a', 'm', 'a', 'n', 'a', 'p', 'l', 'a', 'n', 'a', 'c')

case N is even
('r', 'a', 'c', 'e')
('r', 'a', 'c', 'a')

Which is equivalent to
s[: N // 2 + 1] == s[(N + 1) // 2 - 1 :][::-1]

With this other approach we exclude the middle element for the comparison. This one
seems to be slightly slow than the above one.

H, R = divmod(len(s), 2)
s[:h] == s[: h + r - 1 : -1]

case N is odd
('a', 'm', 'a', 'n', 'a', 'p', 'l', 'a', 'n', 'a')
('a', 'm', 'a', 'n', 'a', 'p', 'l', 'a', 'n', 'a')

case N is even
('r', 'a', 'c', 'e')
('r', 'a', 'c', 'a')

"""

from math import ceil, floor
from re import finditer, sub


class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = sub(r"[\W_]", "", s).lower()
        return s == s[::-1]


class Solution2:
    """No significant improvement compared to first solution"""

    def isPalindrome(self, s: str) -> bool:
        s = sub(r"[\W_]", "", s).lower()
        N = len(s)
        H = N / 2
        return s[: floor(H)] == s[: ceil(H) - 1 : -1]


class Solution3:
    """A slightly better performance"""

    def isPalindrome(self, s: str) -> bool:
        s = sub(r"[\W_]", "", s).lower()
        H, r = divmod(len(s), 2)
        return s[:H] == s[: H + r - 1 : -1]


class Solution4:
    """worst performance."""

    def isPalindrome(self, s: str) -> bool:
        for head, tail in zip(finditer(r"[^\W_]", s), finditer(r"[^\W_]", s[::-1])):
            if head.group().lower() != tail.group().lower():
                return False

        return True


class Solution5:
    """check for string length doesn't help."""

    def isPalindrome(self, s: str) -> bool:
        n = 0

        for head, tail in zip(finditer(r"[^\W_]", s), finditer(r"[^\W_]", s[::-1])):
            n += 1
            # greater than or equal to filtered string
            if n > len(s) // 2:
                return True
            if head.group().lower() != tail.group().lower():
                return False

        return True


class Solution6:
    def isPalindrome(self, s: str) -> bool:
        s = sub(r"[\W_]", "", s).lower()
        N = len(s)
        for i, (h, t) in enumerate(zip(s, reversed(s))):
            if i > N // 2:
                return True
            if h != t:
                return False
        return True


class Solution7:
    def isPalindrome(self, s: str) -> bool:
        s = "".join(c.lower() for c in s if c.isalnum())
        h, r = divmod(len(s), 2)
        return s[:h] == s[: h + r - 1 : -1]


class Solution8:
    def isPalindrome(self, s: str) -> bool:
        """I took this code from leetcode, can't give credit because it doesn't show
        whom did.
        """
        s = "".join(map(lambda x: x.lower() if x.isalnum() else "", s))
        n = len(s)
        return s[: (n - 1) // 2 + 1] == s[n // 2 :][::-1]


class Solution9:
    def isPalindrome(self, s: str) -> bool:
        for h, t in zip(filter(str.isalnum, s), filter(str.isalnum, reversed(s))):
            if h != t:
                return False
        return True


class Solution10:
    def isPalindrome(self, s: str) -> bool:
        s = tuple(c.lower() for c in s if c.isalnum())
        N = len(s)
        return s[: (N - 1) // 2 + 1] == s[N // 2 :][::-1]


class Solution11:
    def isPalindrome(self, s: str) -> bool:
        s = tuple(c.lower() for c in s if c.isalnum())
        N = len(s)
        return s[: N // 2 + 1] == s[(N + 1) // 2 - 1 :][::-1]
