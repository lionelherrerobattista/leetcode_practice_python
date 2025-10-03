# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # BST
        # left subtree < node
        # right subtree > node

        lca = root

        def dfs(node):
            # base case
            if not node:
                return None

            # the current node is the lca
            nonlocal lca
            lca = node

            if node == p or node == q:
                return  # p or q is the lca
            # else traverse
            elif node.val > p.val and node.val > q.val:
                # p and q in the left subtree
                return dfs(node.left)
            elif node.val < p.val and node.val < q.val:
                # p and q in the right subtree
                return dfs(node.right)
            else:
                # found lca
                # split - one in left subtree, other in right subtree
                return

        dfs(root)

        return lca

# Complexity:
# Time: O(h) - height of the tree, choosing only one node by level
# Space: O(h) - height of call stack
