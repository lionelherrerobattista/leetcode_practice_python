from typing import Optional, List
from collections import deque

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # BFS
        nodes = deque([root])  # queue to store nodes
        right_side_nodes = []
        # iterate the tree level by level - Level Order Traversal
        while nodes:
            level_length = len(nodes)
            # iterate nodes in level
            for i in range(level_length):
                node = nodes.popleft()

                if node:
                    # add last node to the list
                    if i == (level_length - 1):
                        right_side_nodes.append(node.val)

                    if node.left:
                        nodes.append(node.left)
                    if node.right:
                        nodes.append(node.right)

        # return list
        return right_side_nodes


sol = Solution()
root = TreeNode(1, TreeNode(2), None)
print(sol.rightSideView(root))

# Complexity:
# Time: O(n) - visit every node
# Space: O(w) - width of the last level
