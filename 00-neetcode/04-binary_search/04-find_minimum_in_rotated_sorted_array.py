from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        # O(log n) -> binary search
        left = 0
        right = len(nums) - 1
        min_num = nums[0]

        while left <= right:
            if nums[left] < nums[right]:
                # all in increasing order
                min_num = min(min_num, nums[left])
                break

            mid = left + ((right - left) // 2)
            min_num = min(min_num, nums[mid])

            # check if min is part of the left sorted portion
            if nums[mid] >= nums[left]:
                # we can discard all to the left
                left = mid + 1
            else:
                # min is in the left sorted portion
                # discard right
                right = mid - 1

        return min_num

# Complexity:
# Time: O(log n) - Binary search
# Space: O(1) - No additional DS


nums = [3, 4, 5, 6, 1, 2]
sol = Solution()
print(sol.findMin(nums))
nums = [1, 2, 3, 4, 5, 6]
print(sol.findMin(nums))
nums = [4, 5, 0, 1, 2, 3]
print(sol.findMin(nums))
nums = [4, 5, 6, 7]
print(sol.findMin(nums))
nums = [2, 1]
print(sol.findMin(nums))
