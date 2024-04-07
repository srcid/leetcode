from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def helper(self, m, n):
        if (m, n) == (None, None):
            return True
        if m is None or n is None:
            return False
        if m.val == n.val and self.helper(m.left, n.right) and self.helper(m.right, n.left):
            return True
        
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root is None or (root.left, root.right) == (None, None):
            return True
        
        return self.helper(root.left, root.right)
