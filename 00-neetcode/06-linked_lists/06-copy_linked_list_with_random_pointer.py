from typing import Optional

# Definition for a Node.


class Node:
    def __init__(self, x: int, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: Optional[Node]) -> Optional[Node]:
        if not head:  # edge case, no head
            return None

        current_node = head
        old_to_copy = {}  # list to map old node to copy

        # loop the list - create node copies and map to old nodes
        while current_node:
            # create node's copy
            node_copy = Node(current_node.val, None, None)
            # map old nodes with its copy
            old_to_copy[current_node] = node_copy
            # continue with next node
            current_node = current_node.next

        # link nodes
        current_node = head
        # new loop to link nodes
        while current_node:
            # get copy
            node_copy = old_to_copy[current_node]
            # update links - account for null pointers
            node_copy.next = old_to_copy[current_node.next] if current_node.next else None
            node_copy.random = old_to_copy[current_node.random] if current_node.random else None
            # continue with next node
            current_node = current_node.next

        return old_to_copy[head]  # return the copy of the head

# Complexity:
# Time: O(n) - we loop through the list, two passes
# Space: O(n) - map for every old node - new node


sol = Solution()
head = Node(3,
            Node(7,
                 Node(4,
                      Node(5,
                           ))))
print(sol.copyRandomList(head))
