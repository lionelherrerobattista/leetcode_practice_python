"""
# Definition for a Node.
"""
from collections import deque
from typing import Optional


class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    # follow up space O(1)
    def connect(self, root: Optional[Node]) -> Optional[Node]:
        # use pointers to keep track of the nodes
        cur, nxt = root, root.left if root else None

        while cur and nxt:
            # connect the next nodes
            cur.left.next = cur.right
            if cur.next: # avoid null cases
                cur.right.next = cur.next.left

            # shift nodes
            cur = cur.next
            if not cur:
                cur = nxt
                nxt = cur.left
        return root


    # solution O(n)
    # def connect(self, root: Optional[Node]) -> Optional[Node]:
    #     if not root:
    #         return root

    #     # save node and right node at the same level
    #     queue = deque([(root, None)])
    #     # traverse bfs
    #     # as we will pass the right node to the next node
    #     while queue:
    #         node, right_node = queue.popleft()
    #         # modify next pointer
    #         node.next = right_node

    #         # check left
    #         # append next node left and it's right node at the same level
    #         if node.left:
    #             queue.append((node.left, node.right))
    #         # check right
    #         # set right node, check if next is not null
    #         # next will have the left node we should set
    #         # unless rightmost nodes => None            
    #         if node.right:
    #             if node.next:
    #                 queue.append((node.right, node.next.left))
    #             else:
    #                 queue.append((node.right, None))

    #     return root

# tests
solution = Solution()
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)
print(solution.connect(root))
        