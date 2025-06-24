from collections import defaultdict
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        path_count = 0
        frequency = {0: 1} # store the frequencies of the sums
        
        def dfs(node, previous_sum):
            nonlocal path_count
            # base case
            if not node:
                return None
            
            # update current sum
            current_sum = previous_sum + node.val

            x = current_sum - targetSum

            # check if the remaining val to complete the sum is in the frequency
            if x in frequency:
                # add to count how many times it appears
                path_count += frequency[x]
            
            # increase frequency
            if current_sum in frequency:
                frequency[current_sum] += 1
            else:
                frequency[current_sum] = 1

            # dfs recursive call
            dfs(node.left, current_sum)
            dfs(node.right, current_sum)

            # after we are done with a branch
            # the current frequency doesn't matter anymore
            # path only downwards
            frequency[current_sum] -= 1

        dfs(root, 0)

        return path_count

# test
solution = Solution()
# Creating the tree
root = TreeNode(10)
root.left = TreeNode(5)
root.right = TreeNode(-3)
root.left.left = TreeNode(3)
root.left.right = TreeNode(2)
root.right.right = TreeNode(11)
root.left.left.left = TreeNode(3)
root.left.left.right = TreeNode(-2)
root.left.right.right = TreeNode(1)
targetSum = 8

# The tree structure will be:
#        10
#       /   \
#      5    -3
#     / \     \
#    3   2    11
#   / \   \
#  3  -2   1

print(solution.pathSum(root, targetSum))

# Creating the tree
root = TreeNode(5)
root.left = TreeNode(4)
root.right = TreeNode(8)
root.left.left = TreeNode(11)
root.left.left.left = TreeNode(7)
root.left.left.right = TreeNode(2)
root.right.left = TreeNode(13)
root.right.right = TreeNode(4)
root.right.right.left = TreeNode(5)
root.right.right.right = TreeNode(1)

targetSum = 22

# The tree structure will be:
#        5
#      /   \
#     4     8
#    /     / \
#  11    13   4
#  / \         / \
# 7   2       5   1

print(solution.pathSum(root, targetSum))