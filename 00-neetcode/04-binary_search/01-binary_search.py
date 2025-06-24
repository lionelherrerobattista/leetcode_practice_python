from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # get pointers to each end of array
        left = 0
        right = len(nums) - 1

        while left <= right:  # if one pointer passes the other
            mid = left + ((right - left) // 2)  # get mid point, avoid overflow

            if nums[mid] > target:
                # look lower part
                right = mid - 1
            elif nums[mid] < target:
                # look upper part
                left = mid + 1
            else:
                return mid  # index of target

        return -1  # target not in array

# Complexity
# Time: O(log n) - each time we remove half the nums
# Space: O(1) - we don't use extra data structures


sol = Solution()
nums = [-1, 0, 2, 4, 6, 8]
target = 4
print(sol.search(nums, target))

nums = [-1, 0, 2, 4, 6, 8]
target = 3
print(sol.search(nums, target))

nums = [-1, 0, 3, 5, 9, 12]
target = 9
print(sol.search(nums, target))
