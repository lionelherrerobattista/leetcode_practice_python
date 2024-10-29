from collections import deque

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def widthOfBinaryTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        max_width = 0
        queue = deque([[root, 1, 0]]) # [node, num, level]
        previous_level = 0
        previous_num = 1 # previous leftmost number
        # BFS:
        while queue:
            node, num, level = queue.popleft()

            # check level
            if level > previous_level:
                previous_level = level
                previous_num = num

            # check the max distance
            max_width = max(max_width, num - previous_num + 1)

            # add node to queue, if not null
            if node.left:
                queue.append([node.left, 2 * num, level + 1]) # 2 * num because it's next level, always 2 * (binary tree)
            if node.right:
                queue.append([node.right, 2 * num + 1, level + 1]) # 2 * num + 1 because it's right node
        
        return max_width