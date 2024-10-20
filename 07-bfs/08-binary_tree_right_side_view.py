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
        answer = []
        if not root:
            return answer
        
        # queue to traverse tree BFS
        # as return values ordered from top to bottom
        queue = deque([root])
        while queue:
            # level order
            size = len(queue)
            last_level_node = None
            # traverse level
            for _ in range(size):
                # keep checking until last level
                last_level_node = queue.popleft()

                # add children
                if last_level_node.left:
                    queue.append(last_level_node.left)
                if last_level_node.right: 
                    queue.append(last_level_node.right)

            if last_level_node: # if node, save value
                answer.append(last_level_node.val)
        return answer
    
solution = Solution()
# Creating the tree
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.right = TreeNode(5)
root.right.right = TreeNode(4)
print(solution.rightSideView(root))
# The tree structure will be:
#       1
#      / \
#     2   3
#      \   \
#       5   4