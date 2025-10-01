from typing import Optional

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # dfs
        is_balanced = True

        def dfs(node):
            if not node:
                return 0

            # post order - get both subtress heights first
            left = dfs(node.left)
            right = dfs(node.right)

            # check the difference between left and right subtrees
            # if it's more than 1 = not balanced
            if abs(left - right) > 1:
                nonlocal is_balanced
                is_balanced = False

            # calculate height and return to parent
            height = 1 + max(left, right)

            return height

        # run function to check if it's balanced
        dfs(root)

        return is_balanced

# Complexity
# Time: O(n) - Visit every node
# Space: O(h) - height of the tree - callstack depth
