from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # base case, no nodes to traverse
        if not preorder or not inorder:
            return None
        
        # create a tree
        root = TreeNode(preorder[0]) # always first value in preorder array
        # find the root's index in inorder array
        # values to the left are left subtree
        # values to the right are right subtree
        mid = inorder.index(preorder[0])
        # left subtree
        # preoder: from index 1 to mid + 1 (not inclusive)
        # preorder: from beginning to mid (not inclusive)
        root.left = self.buildTree(preorder[1:mid + 1], inorder[:mid])
        # right subtree
        # preorder: from mid + 1 until the end
        # inorder: from mid + 1 until the end
        root.right = self.buildTree(preorder[mid + 1:],inorder[mid + 1:])
        # return the root
        return root