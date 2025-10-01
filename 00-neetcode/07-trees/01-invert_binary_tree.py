from typing import Optional

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # traverse to the node
        def dfs(node):
            # base case
            if not node:
                return None
            # invert tree
            aux_node = node.left
            node.left = node.right
            node.right = aux_node

            # traverse both branches recursively
            dfs(node.left)
            dfs(node.right)

        dfs(root)

        return root

# Complexity
# Time: O(n) - Visit each node
# Space: O(h) - Height of call stack O(n) worst case O(log n) average
