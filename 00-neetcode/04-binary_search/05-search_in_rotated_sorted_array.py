from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # O(log n) = binary search
        # two portions, deflection point
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = left + (right - left) // 2

            if target == nums[mid]:
                return mid

            # check if we are in the left sorted portion
            if nums[left] <= nums[mid]:
                # if target is not between left and mid
                if target > nums[mid] or target < nums[left]:
                    left = mid + 1  # search right portion
                else:
                    right = mid - 1  # target is between left and mid, left portion
            else:  # right sorted portion
                # if target is not between right and mid
                if target < nums[mid] or target > nums[right]:
                    right = mid - 1  # search left portion
                else:
                    left = mid + 1  # target is between mid and right, right portion

        return -1

# Complexity
# Time: O(log n) - Binary search
# Space: O(1) - No extra space


sol = Solution()
nums = [3, 4, 5, 6, 1, 2]
target = 1
print(sol.search(nums, target))
nums = [3, 5, 6, 0, 1, 2]
target = 4
print(sol.search(nums, target))
