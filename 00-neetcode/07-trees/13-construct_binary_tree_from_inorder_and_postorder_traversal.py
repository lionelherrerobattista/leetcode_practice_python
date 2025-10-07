from typing import Optional, List

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # base case
        def dfs(preorder, inorder):
            if not preorder or not inorder:
                return None

            # create root node
            root = TreeNode(preorder[0])  # always first in preorder
            mid = inorder.index(preorder[0])  # look for index in inorder

            # create subtrees recursively
            # mid tells us nodes in left and right subtrees
            # we can discard first node in preorder == root
            root.left = self.buildTree(preorder[1:mid + 1], inorder[:mid])
            root.right = self.buildTree(preorder[mid + 1:], inorder[mid + 1:])

            return root

        return dfs(preorder, inorder)

# Complexity
# Time: O(n) - Visit all nodes
# Space: O(h) - Height of call stack
