from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        smallest_values = [] # to add smallest val in tree
        # define dfs function
        # as we need to traverse the tree in-order (left -> root -> right)
        def dfs(node):
            if not node:
                return None
            
            # traverse tree dfs in-order as it's a BST
            # traverse left subtree until leaf
            dfs(node.left)

            # found k smallest
            if len(smallest_values) == k:
                return smallest_values
            else:
                # else, append until k
                smallest_values.append(node.val)
            
            if len(smallest_values) < k:
                dfs(node.right)


            return smallest_values
        dfs(root)
        # return smallest
        return smallest_values[k - 1]
    
# test
solution = Solution()
# Creating the tree
root = TreeNode(5)
root.left = TreeNode(3)
root.right = TreeNode(6)
root.left.left = TreeNode(2)
root.left.right = TreeNode(4)
root.left.left.left = TreeNode(1)
k = 3

# The tree structure will be:
#       5
#      / \
#     3   6
#    / \
#   2   4
#  /
# 1
print(solution.kthSmallest(root, k))