from typing import Optional, List
from collections import deque

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # level order
        # bfs and append each level values
        nodes = deque([root])
        result = []

        # loop tree nodes
        while nodes:
            # traverse each level
            level_list = []
            for _ in range(len(nodes)):
                # from left to right
                current_node = nodes.popleft()
                if current_node:
                    level_list.append(current_node.val)
                    # append left and right pointers
                    if current_node.left:
                        nodes.append(current_node.left)
                    if current_node.right:
                        nodes.append(current_node.right)

            if level_list:
                result.append(level_list)

        return result

# Complexity:
# Time: O(n) - process all the nodes
# Space: O(n) - last level may have (2 * nodes in the tree)
