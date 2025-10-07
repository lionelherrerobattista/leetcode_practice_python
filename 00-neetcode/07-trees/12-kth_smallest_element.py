from typing import Optional

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # bst
        # smallest value should be on the left
        smallest_value = 0
        smallest_counter = 0

        # dfs, reach leftmost value and start to compare
        def dfs(node):
            if not node:
                return None

            # in order traversal
            dfs(node.left)

            # count smallest values
            nonlocal smallest_counter
            smallest_counter += 1

            if k == smallest_counter:
                nonlocal smallest_value
                smallest_value = node.val

            # smallest_values.append(node.val)
            if smallest_counter < k:  # more efficent, still need to find kth
                dfs(node.right)

        dfs(root)
        return smallest_value
