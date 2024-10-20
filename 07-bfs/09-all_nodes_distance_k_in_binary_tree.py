from typing import List
from collections import deque, defaultdict

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        # edge case
        if k == 0:
            return [target.val]
        
        # define graph
        # node:[nodes_reached]
        graph = defaultdict(list)
        # queue for bfs
        queue = deque([root])

        while queue:
            node = queue.popleft()

            if node.left:
                # add to graph
                graph[node].append(node.left)
                # bi directions
                graph[node.left].append(node)

                queue.append(node.left)

            if node.right: # same with right node
                graph[node].append(node.right)
                graph[node.right].append(node)

                queue.append(node.right)
        
        # start bfs
        answer = []
        visited = set([target])
        queue = deque([(target, 0)]) # node, steps

        while queue:
            node, distance = queue.popleft()

            # check the distance
            if distance == k:
                answer.append(node.val)
            else:
                for edge in graph[node]:
                    # visit the other points we can rach
                    if edge not in visited:
                        visited.add(edge)
                        queue.append((edge, distance + 1)) # we take an extra step
        return answer

# complexity
# time: O(n) visit all nodes in the tree
# space: O(n) queue, set,
    
# test
solution = Solution()
root = TreeNode(3)
root.left = TreeNode(5)
root.right = TreeNode(1)
root.left.left = TreeNode(6)
root.left.right = TreeNode(2)
root.right.left = TreeNode(0)
root.right.right = TreeNode(8)
root.left.right.left = TreeNode(7)
root.left.right.right = TreeNode(4)
target = 5
k = 2
print(solution.distanceK(root, root.left, k))