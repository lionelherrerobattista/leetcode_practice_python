from typing import Optional

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # diameter - edges between the longest path
        largest_diameter = 0  # keep track of the max diameter

        def dfs(node):
            # base case
            if not node:
                return 0

            # calculate height of subtrees
            left_height = dfs(node.left)
            right_height = dfs(node.right)

            # calculate diameter (height left + hight right)
            diameter = left_height + right_height

            nonlocal largest_diameter  # to use outer scope variable
            # check if there's new max
            largest_diameter = max(largest_diameter, diameter)

            # calculate height for node's parents 1 + max(left height, right height)
            return 1 + max(left_height, right_height)

        dfs(root)

        return largest_diameter

# Complexity
# Time: O(n) - visit every node
# Space: O(h) - height of the tree
