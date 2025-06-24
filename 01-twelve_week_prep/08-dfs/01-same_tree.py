from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # base cases
        if not p and not q: # both are equal
            return True
        if not p or not q or p.val != q.val: # only one of them is null or different value
            return False
        
        # recursive bfs call
        # both left subtree AND right subtree should be equal => return true
        return (self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right))


        