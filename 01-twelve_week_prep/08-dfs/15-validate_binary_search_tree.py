from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # create dfs function
        # keeps track of min value and max value
        def is_valid(node, min_value, max_value):
            # base case
            if not node:
                return True
            
            # not a valid BST, violates definition
            if node.val <= min_value or node.val >= max_value:
                return False
            
            # when we go to the left, we adjust max value
            # when we go to the right, we adjust min value
            return is_valid(node.left, min_value, node.val) and is_valid(node.right, node.val, max_value)
        
        return is_valid(root, float('-inf'), float('inf'))
            
# complexity:
# Time: O(n)
# Space: O(h)
    # brute force
    # def isValidBST(self, root: Optional[TreeNode]) -> bool:
    #     tree = []
    #     # store all values
    #     def dfs(root):
    #         # base case
    #         if not root:
    #             return None
            
    #         # check if leaf node
    #         if not root.left and not root.right:
    #             return root.val
            
    #         # dfs in-order traversal
    #         left_value = dfs(root.left)
    #         if left_value is not None:
    #             tree.append(left_value)
            
    #         tree.append(root.val)
            
    #         right_value = dfs(root.right)
    #         if right_value is not None:
    #             tree.append(right_value)
    #     # create array recursively
    #     # in-order traversal to create an asc array
    #     dfs(root)

    #     # check if array is ordered
    #     left = 0
    #     while left < len(tree) - 1:
    #         right = left + 1
    #         while right < len(tree):
    #             if tree[left] >= tree[right]:
    #                 # not ordered
    #                 return False
    #             right += 1
    #         left += 1

    #     return True
           
# test
solution = Solution()
# Creating the tree
root = TreeNode(5)
root.left = TreeNode(1)
root.right = TreeNode(4)
root.right.left = TreeNode(3)
root.right.right = TreeNode(6)

print(solution.isValidBST(root))

# Creating the tree
root = TreeNode(2)
root.left = TreeNode(1)
root.right = TreeNode(3)

print(solution.isValidBST(root))

# Creating the tree
root = TreeNode(2)
root.left = TreeNode(2)
root.right = TreeNode(2)

print(solution.isValidBST(root))

# Creating the tree
root = TreeNode(5)
root.left = TreeNode(4)
root.right = TreeNode(6)
root.right.left = TreeNode(3)
root.right.right = TreeNode(7)

print(solution.isValidBST(root))

root = TreeNode(0)

root.right = TreeNode(1)
print(solution.isValidBST(root))

# Creating the tree
root = TreeNode(5)
root.left = TreeNode(0)
root.right = TreeNode(0)

print(solution.isValidBST(root))

