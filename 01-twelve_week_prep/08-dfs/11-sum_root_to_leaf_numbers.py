from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        nums_to_sum = []

        # dfs root -> leaf node:
        def dfs(node, num_string):
            # base case
            if not node:
                return ""
            
            # add num to string
            num_string += str(node.val)
            
            if not node.left and not node.right:
                # leaf node, save number as int
                nums_to_sum.append(int(num_string))

            # dfs subtrees
            dfs(node.left, num_string)
            dfs(node.right, num_string)

        # call function
        dfs(root, "")

        # return the sum of the numbers
        return sum(nums_to_sum)

# complexity
# time: O(n) we need to visit every node in the tree
# space: O(n) recursive approach worst case we will visit the height of the tree = n

# test
solution = Solution()
# Creating the tree
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)

# The tree structure will be:
#       1
#      / \
#     2   3

print(solution.sumNumbers(root))

# Creating the tree
root = TreeNode(4)
root.left = TreeNode(9)
root.right = TreeNode(0)
root.left.left = TreeNode(5)
root.left.right = TreeNode(1)

# The tree structure will be:
#       4
#      / \
#     9   0
#    / \
#   5   1
print(solution.sumNumbers(root))