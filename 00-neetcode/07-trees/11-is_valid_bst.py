from typing import Optional

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def dfs(node, min_value, max_value):
            if not node:
                # no branches, valid bst
                return True

            # bst is invalid when:
            if node.val <= min_value or node.val >= max_value:
                return False

            # check left subtree
            # new max boundary is current node value
            is_valid_left = dfs(node.left, min_value, node.val)
            # check right subtree
            # new min boundary is current node value
            is_valid_right = dfs(node.right, node.val, max_value)

            # both trees should be valid
            return is_valid_left and is_valid_right

        return dfs(root, float("-inf"), float("inf"))

# Complexity
# Time: O(n)
# Space: O(h) - hight of the call stack


sol = Solution()
root = TreeNode(1, TreeNode(2), TreeNode(3))
print(sol.isValidBST(root))
root = TreeNode(1, TreeNode(1))
print(sol.isValidBST(root))
