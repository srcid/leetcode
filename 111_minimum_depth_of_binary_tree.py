# Definition for a binary tree node.
from queue import SimpleQueue
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    @staticmethod
    def isLeaf(node: TreeNode):
        return (node.left, node.right) == (None, None)

    def minDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        q = SimpleQueue()
        q.put(root)
        h = 0

        while True:
            h += 1
            n = q.qsize()

            while n:
                n -= 1
                node = q.get()
                
                if self.isLeaf(node):
                    return h
                if node.left != None:
                    q.put(node.left)
                if node.right != None:
                    q.put(node.right)
