from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        counts = [0, 0, 0]  # counts of colors

        # get the counts
        for color in nums:
            counts[color] += 1

        # unpack the counts
        R, W, B = counts

        # replace regions
        nums[:R] = [0] * R
        nums[R:R+W] = [1] * W
        nums[R+W:] = [2] * B

# Complexity
# Time: O(n)
# Space: O(1)


# TEST
solution = Solution()
nums = [2, 0, 2, 1, 1, 0]
solution.sortColors(nums)
print(nums)
nums = [2, 0, 1]
solution.sortColors(nums)
print(nums)
