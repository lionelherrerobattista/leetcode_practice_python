from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = left + (right - left) // 2 # avoid overflow

            # check if target
            if nums[mid] == target:
                return True
            
            if nums[left] < nums[mid]: # if we are in left portion
                if nums[left] <= target and nums[mid] > target:
                    right = mid - 1 # continue searching left
                else:
                    left = mid + 1
            elif nums[left] > nums[mid]: # right portion
                if nums[mid] < target and nums[right] >= target:
                    left = mid + 1 # continue searching right
                else:
                    right = mid - 1
            else: # values are equal, we can determine position
                left += 1 # move left by 1, best we can do

        return False
    

solution = Solution()
nums = [2,5,6,0,0,1,2]
target = 0
print(solution.search(nums, target))
nums = [2,5,6,0,0,1,2]
target = 3
print(solution.search(nums, target))
nums = [1]
target = 0
print(solution.search(nums, target))
