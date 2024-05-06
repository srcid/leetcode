from typing import List, Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self) -> str:
        val = self.val
        next = self.next
        return f"{val}, {next}"


class Solution:
    @staticmethod
    def merge(l: ListNode, r: ListNode) -> ListNode:
        if None in (l, r):
            return l or r

        merged = None
        cur = merged

        while l and r:
            if cur is None:
                cur = ListNode()
                merged = cur
            else:
                cur.next = ListNode()
                cur = cur.next

            if l.val <= r.val:
                cur.val = l.val
                l = l.next
            else:
                cur.val = r.val
                r = r.next

        cur.next = l or r

        return merged

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0:
            return None

        if len(lists) == 1:
            return lists[0]

        ans = None

        for l in lists:
            ans = self.merge(ans, l)
            print(ans)

        return ans


if __name__ == "__main__":
    lists = [
        ListNode(1, ListNode(4, ListNode(5))),
        ListNode(1, ListNode(3, ListNode(4))),
        ListNode(2, ListNode(6)),
    ]
    s = Solution()
    print(s.mergeKLists(lists))
