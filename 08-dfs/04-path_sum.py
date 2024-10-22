
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        # base case
        if not root:
            return False
        
        # decrease from target sum
        targetSum -= root.val
        
        # leaf node
        if not root.left and not root.right:
            return targetSum == 0 # if value is 0 we found the path to leaf node

        # return the result of dfs
        # if either path has the sum == targetSum return True, else False
        return self.hasPathSum(root.left, targetSum) or self.hasPathSum(root.right, targetSum)

# test
solution = Solution()
# Creating the tree
root = TreeNode(5)
root.left = TreeNode(4)
root.right = TreeNode(8)
root.left.left = TreeNode(11)
root.left.left.left = TreeNode(7)
root.left.left.right = TreeNode(2)
root.right.left = TreeNode(13)
root.right.right = TreeNode(4)
root.right.right.right = TreeNode(1)
targetSum = 22
print(solution.hasPathSum(root, targetSum))
# The tree structure will be:
#        5
#      /   \
#     4     8
#    /     / \
#   11   13   4
#  / \         \
# 7   2         1