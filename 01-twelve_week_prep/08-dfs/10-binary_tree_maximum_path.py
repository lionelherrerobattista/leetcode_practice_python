from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_sum = root.val
        def dfs(root):
            nonlocal max_sum # avoid error
            # base case
            if not root:
                return 0 # no val to sum
            
            # check the values on the left and right subtrees
            left_max = dfs(root.left) 
            right_max = dfs(root.right)
            # if the value is negative, convert it to 0
            # we don't want to sum negative numbers
            left_max = max(left_max, 0)
            right_max = max(right_max, 0)

            # check the max path WITH a split
            # current node is path's root
            # (we can only split once)
            max_sum = max(max_sum, root.val + left_max + right_max)

            # return value if we don't split
            # using only one of the subtrees
            return root.val + max(left_max, right_max)
        
        # call recursive function
        dfs(root)

        return max_sum

# test
solution = Solution()
# Creating the tree
root = TreeNode(-10)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)
print(solution.maxPathSum(root))

# The tree structure will be:
#       -10
#       /  \
#     9    20
#         /  \
#       15    7
            
# Creating the tree
root = TreeNode(-2)
root.right = TreeNode(-3)

# The tree structure will be:
#       -2
#         \
#         -3
print(solution.maxPathSum(root))

