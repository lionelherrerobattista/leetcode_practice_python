from collections import deque

# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    # solution O(1) space:
    def connect(self, root: 'Node') -> 'Node':
        leftmost = root # keep track of the leftmost node in each iteration

        # traverse tree
        while leftmost: # when we don't have one, we reach the end of the tree
            current_node = leftmost # we start from left
            leftmost = None
            previous_node = None # to update next pointer

            # traverse level
            while current_node:
                # check left branch
                if current_node.left:
                    if not leftmost: # check if node's first level
                        leftmost = current_node.left
                    
                    # update next
                    if previous_node:
                        previous_node.next = current_node.left
                    
                    # save the previous node for next iteration
                    previous_node = current_node.left

                # check right branch
                if current_node.right:
                    # same as left child
                    if not leftmost:
                        leftmost = current_node.right
                    
                    if previous_node:
                        previous_node.next = current_node.right

                    previous_node = current_node.right

                # now we check the node to the right (same level)
                current_node = current_node.next
        
        return root


    # solution O(n) time and space
    # def connect(self, root: 'Node') -> 'Node':
    #     # check edge case, empty root
    #     if not root:
    #         return root

    #     # create queue for nodes
    #     queue = deque([root])
    #     # traverse the tree BFS
    #     while queue:
    #         # level order traversal
    #         size = len(queue) # length of level
    #         previous_node = None # save previous node to assign
    #         # traverse level
    #         for _ in range(size):
    #             node = queue.popleft()
    #             # we set the previous node's next value
    #             # to rightmost node
    #             if previous_node:
    #                 previous_node.next = node
    #             # append children, if any
    #             if node.left:
    #                 queue.append(node.left)
    #             if node.right:
    #                 queue.append(node.right)
    #             # change previous node for next iteration
    #             previous_node = node
    #     return root

# test
solution = Solution()
# Creating the tree
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.right = Node(7)
print(solution.connect(root))

# The tree structure will be:
#       1
#      / \
#     2   3
#    / \   \
#   4   5   7