# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        #base case
        if not root:
            return None
        
        # if we found p or q
        if root.val == p.val or root.val == q.val:
            return root # return it
                    
        # check subtrees bfs
        # return the first to appear if they are in same subtree
        # return both in different subtrees
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        if left and right: # both non null, different subtrees of current node
            return root # the current node is the common ancestor
        elif left and not right: # the non-null is the LCA
            return left
        else:
            return right
      

# test
solution = Solution()
# Creating the tree
root = TreeNode(3)
root.left = TreeNode(5)
root.right = TreeNode(1)
root.left.left = TreeNode(6)
root.left.right = TreeNode(2)
root.right.left = TreeNode(0)
root.right.right = TreeNode(8)
root.left.right.left = TreeNode(7)
root.left.right.right = TreeNode(4)
# The tree structure will be:
#        3
#      /   \
#     5     1
#    / \   / \
#   6   2 0   8
#      / \
#     7   4
p = TreeNode(5)
q = TreeNode(1)
print(solution.lowestCommonAncestor(root, p, q))