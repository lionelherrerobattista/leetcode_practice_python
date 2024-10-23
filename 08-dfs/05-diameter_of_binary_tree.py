from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self.largest_diameter = 0 # memeber variable to get max height
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # largest_diameter = 0 # variable to get max heights

        # dfs to return height of tree
        def dfs(curr):
            # base case
            if not curr:
                return 0
            
            # check height of left and right subtrees
            left_height = dfs(curr.left)
            right_height = dfs(curr.right)
            diameter = left_height + right_height

            # sum both and check if greater than current diameter
            # nonlocal largest_diameter
            self.largest_diameter = max(self.largest_diameter, diameter)
            
            # return current max diameter
            return 1 + max(left_height, right_height) # 1+ because we add the root node of the subtrees

        dfs(root)
        
        return self.largest_diameter
    
# Creating the tree
solution = Solution()
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
print(solution.diameterOfBinaryTree(root))

# The tree structure will be:
#       1
#      / \
#     2   3
#    / \
#   4   5
        