from typing import Optional, List
from collections import deque
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        answer = []
        # queue to traverse the tree
        queue = deque([root])

        # start traversing the tree
        while queue:
            # by level BFS
            total = 0
            size = len(queue)
            # traverse each node in the level
            for _ in range(size):
                node = queue.popleft()
                # acumulate values
                total += node.val
                # check the children and append them to the queue
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            # get the average of values
            average = total / size
            answer.append(average)
        return answer
    
# Complexity 
# Time: O(n)
# Space: O(n)
    
solution = Solution()
# Creating the tree
root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)
print(solution.averageOfLevels(root))

        