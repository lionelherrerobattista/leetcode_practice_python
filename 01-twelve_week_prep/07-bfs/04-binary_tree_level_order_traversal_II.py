from collections import deque
from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        answer = []
        # edge case
        if not root:
            return answer
        # traverse bfs
        queue = deque([root])
        reverse_stack = []

        while queue:
            # get node
            size = len(queue)
            level = []

            # traverse level left to right
            for _ in range(size):
                # check values
                node = queue.popleft()

                # add value to level
                level.append(node.val)

                # append next level to stack
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            #add level to stack
            reverse_stack.append(level)
        
        # pop stack and return answer
        while reverse_stack:
            answer.append(reverse_stack.pop())

        return answer

# tests
solution = Solution()
# Creating the tree
root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)
print(solution.levelOrderBottom(root))