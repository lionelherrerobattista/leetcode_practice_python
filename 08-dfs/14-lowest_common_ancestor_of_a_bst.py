

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        lca = root
        def dfs(node):
            nonlocal lca
            # base case
            if not node:
                return
             
            lca = node

            # lca is p or q
            if node is p or node is q:
                return
            elif node.val < p.val and node.val < q.val:
                # search left (BST property)
                dfs(node.right)
            elif node.val > p.val and node.val > q.val:
                # search right (BST property)
                dfs(node.left)
            else:
                # the value is in between, current node is best lca
                return
        # call to recursive func
        dfs(root)
        # return lca
        return lca
    
# complexity
# Time: O(h) height of the tree
# Space: O(h) recursive, height
# test
solution = Solution()
# Creating the tree
root = TreeNode(6)
root.left = TreeNode(2)
root.right = TreeNode(8)
root.left.left = TreeNode(0)
root.left.right = TreeNode(4)
root.right.left = TreeNode(7)
root.right.right = TreeNode(9)
root.left.right.left = TreeNode(3)
root.left.right.right = TreeNode(5)
p = TreeNode(2)
q = TreeNode(8)
# The tree structure will be:
#       6
#      / \
#     2   8
#    / \ / \
#   0  4 7  9
#     / \
#    3   5

print(solution.lowestCommonAncestor(root, p, q))

p = TreeNode(2)
q = TreeNode(4)
print(solution.lowestCommonAncestor(root, p, q))