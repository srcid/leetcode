from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False

        s = [(root, root.val)]

        while len(s):
            node, acc = s.pop()

            if acc == targetSum and (node.left, node.right) == (None, None):
                return True

            s.extend(
                (treeNode, acc + treeNode.val)
                for treeNode in filter(None, (node.left, node.right))
            )

        return False
