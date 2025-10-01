from typing import Optional

# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # like a sum we need to take account of the carry
        l1_pointer = l1
        l2_pointer = l2

        dummy = ListNode()
        previous_node = dummy
        carry = 0  # account for carry between nodes, max 2 digits

        # iterate through the linked lists
        while l1_pointer or l2_pointer:  # or carry
            # store numbers in the array
            pointer_l1_val = l1_pointer.val if l1_pointer else 0
            pointer_l2_val = l2_pointer.val if l2_pointer else 0
            sum_val = pointer_l1_val + pointer_l2_val + carry

            # check if more than 1 digit
            # max 2 digits, e.g. 18
            last_digit = sum_val % 10  # e.g: 8
            carry = sum_val // 10  # e.g: 1

            # create new node
            node = ListNode()
            node.val = last_digit
            previous_node.next = node

            # update pointers
            previous_node = node

            # move to next node
            l1_pointer = l1_pointer.next if l1_pointer else None
            l2_pointer = l2_pointer.next if l2_pointer else None

        if carry > 0:  # if there is carry left after sum
            # create new node
            node = ListNode()
            node.val = carry
            previous_node.next = node

        # return head
        return dummy.next

# Complexity
# Time: O(n + m) - loop through all the lists nodes
# Space: O(1) - No need of extra space
