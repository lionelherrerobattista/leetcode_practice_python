from typing import List, Optional

# Definition for a binary tree node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        def createTree(nums_array):
            # base case, empty array
            if not nums_array:
                return None
        
            # find max in array:
            max_node = nums_array[0]
            for num in nums_array:
                if num > max_node:
                    max_node = num

            # get index of max in nums
            index_of_max = nums_array.index(max_node)
            # create node
            current_root = TreeNode(max_node)
            
            # assign left subtree recursively
            # ends befor index of max element
            current_root.left = createTree(nums_array[:index_of_max])
            # assign right subtree
            # from index of max + 1 until the end
            current_root.right = createTree(nums_array[index_of_max + 1:])
            # return the current root
            return current_root
        
        return createTree(nums)

# Complexity
# Time: O(n^2)
# Space: O(n)

# test
solution = Solution()
nums = [3,2,1,6,0,5]
solution.constructMaximumBinaryTree(nums)