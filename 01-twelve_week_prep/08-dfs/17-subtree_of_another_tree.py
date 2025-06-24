from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def isSameTree(node_one, node_two):

            if not node_one and not node_two:
                return True
            
            # any node is null and the other is not
            if ((not node_one and node_two) or
                (not node_two and node_one)):
                return False
            
            # check value
            if node_one.val != node_two.val:
                return False

            # both should be true
            return isSameTree(node_one.left, node_two.left) and isSameTree(node_one.right, node_two.right)


        def dfs(node):
            if not node:
                return False
            
            # check if we found root
            if node.val == subRoot.val and isSameTree(node, subRoot):
                return True
            
            # one of them should be true
            return dfs(node.left) or dfs(node.right)
        # return result of dfs
        return dfs(root)

# complexity
# Time: O(m * n) two trees
# Space: O(m + n)

# test
solution = Solution()
# Creating the tree
root = TreeNode(10)
root.left = TreeNode(4)
root.right = TreeNode(5)
root.left.left = TreeNode(1)
root.left.right = TreeNode(2)

subRoot = TreeNode(4)
subRoot.left = TreeNode(1)
subRoot.right = TreeNode(2)

print(solution.isSubtree(root, subRoot))
