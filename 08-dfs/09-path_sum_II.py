from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        answer = []
        def dfs(node: Optional[TreeNode], root_to_leaf_path: List):
            # base case
            if not node:
                return None
            
            # push node value
            root_to_leaf_path.append(node.val)
            
            # check if leaf node
            if not node.left and not node.right:
                # check if values equal target sum
                if sum(root_to_leaf_path) == targetSum:
                    # append to answer array
                    answer.append(root_to_leaf_path)
                return node
            
            # dfs call on subtrees
            dfs(node.left, root_to_leaf_path.copy())
            dfs(node.right, root_to_leaf_path.copy())

            return node
        # call to recursive function
        dfs(root, [])
        # return final answer
        return answer
                
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
root.right.right.left = TreeNode(5)
root.right.right.right = TreeNode(1)
targetSum = 22
# The tree structure will be:
#        5
#      /   \
#     4     8
#    /     / \
#   11    13  4
#  /  \       / \
# 7    2     5   1
print(solution.pathSum(root, targetSum))

            
