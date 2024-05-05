from typing import List, Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    @staticmethod
    def insertListNode(root, val):
        if root is None:
            return ListNode(val)

        root.next = ListNode(val)
        return root.next

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0:
            return None

        if len(lists) == 1:
            return lists[0]

        ans = None
        root = ans

        while True:
            ie = min(
                ((i, node.val) for i, node in enumerate(lists) if node is not None),
                default=None,
                key=lambda t: t[1],
            )

            if ie is None:
                break

            i, e = ie
            root = self.insertListNode(root, e)

            if ans is None:
                ans = root

            lists[i] = lists[i].next

        return ans
