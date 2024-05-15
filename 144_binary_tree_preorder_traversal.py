from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class SolutionRecursive:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        return (
            []
            if root is None
            else [
                root.val,
                *self.preorderTraversal(root.left),
                *self.preorderTraversal(root.right),
            ]
        )


class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []

        if root is None:
            return ans

        stack = [root]

        while len(stack) > 0:
            node = stack.pop()
            ans.append(node.val)
            stack.extend(filter(None, (node.right, node.left)))

        return ans
