from typing import Optional

# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # Use 2 "pointers"
        # 1. list1
        # 2. list2
        head = ListNode()  # dummy node to avoid edge case
        tail = head  # to keep track of the tail
        list1_pointer = list1
        list2_pointer = list2

        # Iterate and move the pointers until both point to None
        while list1_pointer is not None and list2_pointer is not None:
            # Compare, and look for smallest or equal
            if list1_pointer.val <= list2_pointer.val:
                # add to the new list
                tail.next = list1_pointer
                list1_pointer = list1_pointer.next
            else:
                tail.next = list2_pointer
                list2_pointer = list2_pointer.next
            # replace new list node with added node to continue the chain
            tail = tail.next

        if list1_pointer is not None and list2_pointer is None:
            tail.next = list1_pointer
        elif list2_pointer is not None and list1_pointer is None:
            tail.next = list2_pointer

        # We return the list
        return head.next  # return list without dummy

# Complexity
# Time: O(n) - touch each element
# Space: O(n + m) - new list with size of the 2 lists combined


list1 = (ListNode(1,
                  ListNode(2,
                           ListNode(4))))
list2 = (ListNode(1,
                  ListNode(3,
                           ListNode(5))))
sol = Solution()
print(sol.mergeTwoLists(list1, list2))
