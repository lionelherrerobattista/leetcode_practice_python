from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    # better solution
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # base case
        if not root:
            return 0
        
        # recursive bfs call to subtrees
        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)

        # max height formula: current node + max(left subtree, right subtree)
        return 1 + max(left, right)

    # my solution
    # def maxDepth(self, root: Optional[TreeNode]) -> int:
    #     max_depth = 0
    #     def dfs(node, node_count):
    #         # base case
    #         if not node:
    #             return None
            
    #         # increase count
    #         node_count += 1
            
    #         # check if new max
    #         nonlocal max_depth
    #         if node_count > max_depth:
    #             max_depth = node_count

    #         # dfs
    #         # check left and right subtrees, 
    #         # pass current node count
    #         dfs(node.left, node_count)
    #         dfs(node.right, node_count)

    #         return max_depth
        
    #     # execute dfs function and return max_depth
    #     dfs(root, 0)
    #     return max_depth

# test
solution = Solution()
# Creating the tree
root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)
print(solution.maxDepth(root))

# The tree structure will be:
#       3
#      / \
#     9   20
#        /  \
#       15   7



