from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        
        # create new tree and invert left and right
        node = TreeNode(root.val)
        # dfs and connect to inverse subtrees
        node.right = self.invertTree(root.left)
        node.left = self.invertTree(root.right)

        return node

# complexity
# time: O(n) we have to visit all the nodes in the tree
# space: O(n) n => height of the tree as it is a recursive function

# test
solution = Solution()
# Creating the tree
root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(7)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)
root.right.left = TreeNode(6)
root.right.right = TreeNode(9)

# The tree structure will be:
#       4
#      / \
#     2   7
#    / \ / \
#   1  3 6  9

solution.invertTree(root)