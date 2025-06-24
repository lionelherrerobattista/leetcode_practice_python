from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target: # found the target
                return mid
            
            # check if we are in:
            # left sorted portion
            if nums[left] <= nums[mid]:
                # check leftmost value
                if target > nums[mid] or target < nums[left]:
                    left = mid + 1 # eliminate left
                else:
                    right = mid - 1
            # right sorted portion
            else:
                # check rightmost element
                if target < nums[mid] or target > nums[right]:
                    right = mid - 1 # eliminate right
                else:
                    left = mid + 1
        return -1

# tests
solution = Solution()    
nums = [4,5,6,7,0,1,2]
target = 0
print(solution.search(nums, target))
nums = [4,5,6,7,0,1,2]
target = 3
print(solution.search(nums, target))
nums = [1]
target = 0
print(solution.search(nums, target))
nums = [1,3]
target = 0
print(solution.search(nums, target))
nums = [1,3]
target = 3
print(solution.search(nums, target))
nums = [3, 1]
target = 1
print(solution.search(nums, target))