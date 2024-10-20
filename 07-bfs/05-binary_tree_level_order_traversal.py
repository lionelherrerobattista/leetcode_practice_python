# Definition for a binary tree node.
from collections import deque
from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        answer = []
        # edge case
        if not root:
            return answer
        
        # queue to traverse the tree BFS
        queue = deque([root])

        # traverse the tree
        while queue:
            # store values by level
            level = []
            size = len(queue)
            # traverse level
            for _ in range(size):
                # get value from the node
                node = queue.popleft()
                level.append(node.val)
                # push the childern nodes to the queue
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            # push level to answer
            answer.append(level)
        return answer

# Complexity:
# Time: O(n)
# Space: O(n)
# test
solution = Solution()
# Creating the tree
root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)
print(solution.levelOrder(root))

