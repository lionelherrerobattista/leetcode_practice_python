from typing import Optional

# Definition for singly-linked list.


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # create two pointers, fast and slow
        fast = head  # moves 2 nodes at a time
        slow = head  # moves 1 node

        # Iterate through the array
        while fast and fast.next:
            # update pointers
            slow = slow.next
            fast = fast.next.next

            # if the two pointers meet, there is a cycle
            if fast == slow:
                return True

        # end without pointers meeting
        # no cycle
        return False

# Complexity:
# Time: O(n) - Time to reduce the gap between the two pointers
# Space: O(1) - No extra memory needed
