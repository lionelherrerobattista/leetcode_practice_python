from typing import Optional

# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # count the nodes, greedy approach
        dummy = ListNode(0, head)  # create dummy to avoid edge case
        left_pointer = dummy
        right_pointer = head
        count = 0

        # use right pointer to reach nth node
        while right_pointer and count < n:
            count += 1
            right_pointer = right_pointer.next

        # start the left pointer
        # will stop one node before the node to remove
        while right_pointer:
            right_pointer = right_pointer.next
            left_pointer = left_pointer.next

        # remove the node
        node_to_remove = left_pointer.next
        # always valid, at least one node + dummy
        left_pointer.next = node_to_remove.next

        return dummy.next  # return next from dummy

# Complexity
# Time: O(n) - we iterate through the list once
# Space: O(1) - no extra space needed


sol = Solution()
head = ListNode(1,
                ListNode(2,
                         ListNode(3,
                                  ListNode(4))))
sol.removeNthFromEnd(head, 2)
head = ListNode(5)
sol.removeNthFromEnd(head, 1)
head = ListNode(1,
                ListNode(2))
sol.removeNthFromEnd(head, 2)
