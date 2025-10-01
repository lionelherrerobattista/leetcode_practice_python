from collections import deque
from typing import Optional

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # bfs
        # traverse trees at the same time
        # to compare each node of the trees
        p_nodes = deque([p])
        q_nodes = deque([q])

        # traverse trees
        while p_nodes and q_nodes:
            # process the level
            for _ in range(len(p_nodes)):
                # get nodes
                p_node = p_nodes.popleft()
                q_node = q_nodes.popleft()

                if not p_node and not q_node:
                    # both null, leaf node
                    continue
                elif (not p_node and q_node) or (p_node and not q_node):
                    return False  # different tree
                elif p_node.val != q_node.val:
                    return False  # different tree
                else:
                    # same value, add new nodes
                    p_nodes.append(p_node.left)
                    p_nodes.append(p_node.right)
                    q_nodes.append(q_node.left)
                    q_nodes.append(q_node.right)

        return True

# Complexity
# Time: O(p + q) - visit each node in both trees
# Space: O(n) - queue
