from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: Optional[ListNode], visited=None) -> bool:
        visited = visited or []

        if head is None or head.next is None:
            return False

        if head in visited:
            return True

        visited.append(head)

        return self.hasCycle(head.next, visited)
