from typing import Optional

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        # helper to find equal
        def is_same_tree(node_tree, node_subtree):
            if not node_tree and not node_subtree:
                return True
            if (not node_tree and node_subtree) or (node_tree and not node_subtree):
                return False
            if node_tree.val != node_subtree.val:
                return False

            left_subtree = is_same_tree(node_tree.left, node_subtree.left)
            right_subtree = is_same_tree(node_tree.right, node_subtree.right)

            # are subtrees equal? both should be equal (and)
            return left_subtree and right_subtree

        # helper to find subroot
        def has_subtree(root, subRoot):
            if not root:
                return False

            # pre-order
            # check if it's the same tree
            if is_same_tree(root, subRoot):  # handle case, root and subtree same value
                return True

            # check both branches
            # subtree may be in either branch (or)
            left_branch = has_subtree(root.left, subRoot)
            right_branch = has_subtree(root.right, subRoot)

            return left_branch or right_branch

        return has_subtree(root, subRoot)

# Complexity
# Time: O(n * m) - for every node in the root we may check every node in subroot
# Space: O(m + n)
