# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return False

        match root.val:
            case 0 | 1:
                return bool(root.val)
            case 2:
                return self.evaluateTree(root.left) or self.evaluateTree(root.right)
            case _:
                return self.evaluateTree(root.left) and self.evaluateTree(root.right)
