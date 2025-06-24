from collections import deque
from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        answer = []
        # edge case
        if not root:
            return answer
         
        queue = deque([root])
        flag = True # check if we should reverse order or not

        while queue:
            size = len(queue)
            level = [] # to store left to right elements
            reverse_stack = [] # to store right to left elements

            # traverse the level
            for _ in range(size):
                node = queue.popleft()

                # check flag to reverse values
                if flag:
                    reverse_stack.append(node.val)
                else:
                    level.append(node.val)

                # add nodes to queue
                if node.right:
                    queue.append(node.right)
                if node.left:
                    queue.append(node.left)
            # change flag to achieve zigzag
            flag = not flag

            # pop the elements from stack
            while reverse_stack:
                level.append(reverse_stack.pop())

            # append the level's values to the list
            answer.append(level)
        return answer
    
# tests
solution = Solution()
root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)
print(solution.zigzagLevelOrder(root))