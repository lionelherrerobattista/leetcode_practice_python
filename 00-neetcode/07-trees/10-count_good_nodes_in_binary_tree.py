# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # DFS
        good_nodes = 0  # root is a good node

        def dfs(node, greatest_value):  # keep track of greatest value
            if not node:
                return

            # pre order traversal
            if node.val >= greatest_value:
                nonlocal good_nodes
                good_nodes += 1

            # keep track of max value
            max_value = max(greatest_value, node.val)

            # traverse tree,
            dfs(node.left, max_value)
            dfs(node.right, max_value)

        # run recursive function
        dfs(root, root.val)

        return good_nodes
