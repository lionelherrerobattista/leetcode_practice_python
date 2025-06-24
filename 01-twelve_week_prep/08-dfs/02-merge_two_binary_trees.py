from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        # merge everything into new tree
        # base case
        if not root1 and not root2: # null trees
            return None

        # assign node's values
        # if no node, default value of 0
        value1 = root1.val if root1 else 0
        value2 = root2.val if root2 else 0
        # create new node from values
        root = TreeNode(value1 + value2)

        # bfs call, traverse left subtree and right subtree for each node
        # check for null nodes
        root.left = self.mergeTrees(root1.left if root1 else None, root2.left if root2 else None)
        root.right = self.mergeTrees(root1.right if root1 else None, root2.right if root2 else None)

        return root

# test
solution = Solution()
# Creating the first tree
root1 = TreeNode(1)
root1.left = TreeNode(3)
root1.right = TreeNode(2)
root1.left.left = TreeNode(5)

# The tree structure will be:
#       1
#      / \
#     3   2
#    /
#   5

# Creating the second tree
root2 = TreeNode(2)
root2.left = TreeNode(1)
root2.right = TreeNode(3)
root2.left.right = TreeNode(4)
root2.right.right = TreeNode(7)

# The tree structure will be:
#       2
#      / \
#     1   3
#      \   \
#       4   7

print(solution.mergeTrees(root1, root2))
