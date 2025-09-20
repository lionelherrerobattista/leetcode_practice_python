from typing import Optional

# Definition for singly-linked list.


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # create a list to store the visited nodes
        visited_nodes = []
        current_node = head
        # use pointer to iterate through the list
        while current_node is not None:
            # if current node is in visited return true
            if current_node in visited_nodes:
                return True
            # Store node in visited array
            visited_nodes.append(current_node)
            # update current node, with next node
            current_node = current_node.next
        # if no return, no cycle return false
        return False
