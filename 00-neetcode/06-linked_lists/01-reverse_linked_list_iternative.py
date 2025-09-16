from typing import Optional

# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return head

        current_node = head  # current node pointer
        previous_node = None  # previous node pointer

        while current_node is not None:
            aux_node = current_node.next  # store it momentarily
            # point next to previous node
            current_node.next = previous_node
            # current is next previous node
            previous_node = current_node
            # current node is the next link
            current_node = aux_node

        return previous_node  # will be the new head, current_node is None

# Complexity
# Time: O(n) - Iterate through the linked list
# Space: O(1) - No extra space
