from typing import Optional

# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # Store visited values y a list
        visited_nodes = []
        current_node = head

        while current_node:
            visited_nodes.append(current_node)
            current_node = current_node.next

        # two pointers, one at the beginning and one at the end
        right_pointer = len(visited_nodes) - 1
        for left_pointer in range(0, len(visited_nodes)):
            # change next values of the nodes
            right_node = visited_nodes[right_pointer]
            left_node = visited_nodes[left_pointer]
            # insert node in between
            right_node.next = left_node.next
            left_node.next = right_node

            right_pointer -= 1

            if right_pointer <= left_pointer:
                right_node.next = None
                break

# Complexity
# Time: O(n) - visit each node, two times
# Space: O(n) - list to store visited nodes


head = ListNode(0,
                ListNode(1,
                         ListNode(2,
                                  ListNode(3,
                                           ListNode(4,
                                                    ListNode(5,
                                                             ListNode(6)))))))
sol = Solution()
print(sol.reorderList(head))
