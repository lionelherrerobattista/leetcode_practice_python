from typing import Optional

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # use dfs to traverse tree
        # store the depth as we traverse the tree
        def dfs(node, depth):
            # base case
            if not node:
                return depth

            # add 1 to depth, as we go down each level
            depth += 1

            # executre recursively
            # and store depth of each branch
            depth_left_subtree = dfs(node.left, depth)
            depth_right_subtree = dfs(node.right, depth)

            # check larger depth and return
            return max(depth_left_subtree, depth_right_subtree)

        # run recursive function
        depth_tree = dfs(root, 0)  # starting node, depth

        return depth_tree

# Complexity
# Time: O(n) - Visit each node
# Space: O(h) - height of the tree, call stack
