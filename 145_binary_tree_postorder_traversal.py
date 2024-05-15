from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class SolutionRec:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        return (
            []
            if root is None
            else [
                *self.postorderTraversal(root.left),
                *self.postorderTraversal(root.right),
                root.val,
            ]
        )


class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []

        if root is None:
            return ans

        stack = [root]

        while len(stack):
            node = stack.pop()
            stack.extend(filter(None, (node.left, node.right)))
            ans.append(node.val)

        return ans[::-1]
