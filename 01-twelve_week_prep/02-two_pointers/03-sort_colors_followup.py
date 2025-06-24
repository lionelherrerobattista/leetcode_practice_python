from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left, right = 0, len(nums) - 1
        i = 0  # iterates through entire array

        def swap(i, j):
            """function to swap numbers"""
            tmp = nums[i]
            nums[i] = nums[j]
            nums[j] = tmp

        while i <= right:

            if nums[i] == 0:  # check left
                swap(left, i)
                # move pointer
                left += 1
            elif nums[i] == 2:  # check right
                swap(i, right)
                # move pointer
                right -= 1
                # if we encounter a 2 don't increment i
                i -= 1  # to cancel next increment
            # continue checking next numbers
            i += 1
# Complexity
# Time: O(n log n)
# Space: O(1)


# TEST
solution = Solution()
nums = [2, 0, 2, 1, 1, 0]
solution.sortColors(nums)
print(nums)
nums = [2, 0, 1]
solution.sortColors(nums)
print(nums)
