from collections import Counter, defaultdict
from functools import partial
from typing import List


class MyCounter(Counter):
    def __hash__(self) -> int:
        return hash(tuple(sorted(self.items())))


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = defaultdict(list)

        for s in strs:
            # frozenset do not work because we need to address the occurrencies of each word
            n = MyCounter(s)
            ans[n].append(s)

        return ans.values()


def pipe(*funcs):
    def inner(val):
        for f in funcs:
            val = f(val)

        return val

    return inner


# This was faster
class Solution2:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = defaultdict(list)
        getindex = pipe(sorted, partial(str.join, ""))

        for s in strs:
            n = getindex(s)
            ans[n].append(s)

        return ans.values()


if __name__ == "__main__":
    strs_list = [
        ["eat", "tea", "tan", "ate", "nat", "bat"],
        [""],
        ["a"],
        ["cab", "tin", "pew", "duh", "may", "ill", "buy", "bar", "max", "doc"],
        ["ddddddddddg", "dgggggggggg"],
    ]

    s = Solution2()

    for strs in strs_list:
        ans = s.groupAnagrams(strs)
        print(ans)
