from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2

            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid # when left == right we found the min
        return nums[left]

# My solution:
# class Solution:
#     def findMin(self, nums: List[int]) -> int:
#         left, right = 0, len(nums) - 1
#         min_value = 5001

#         while left <= right:
#             mid = left + (right - left) // 2

#             # check new min value
#             if nums[mid] < min_value:
#                 min_value = nums[mid]
#             # move pointer
#             if nums[left] > nums[right]:
#                 if nums[left] > nums[mid]: # if the pivot is between left and mid
#                     right = mid - 1
#                 else:
#                     # min values are on the right side
#                     left = mid + 1
#             else:
#                 right = mid - 1
#         return min_value

# test
solution = Solution()
nums = [3,4,5,1,2]
print(solution.findMin(nums))
nums = [4,5,6,7,0,1,2]
print(solution.findMin(nums))
nums = [11,13,15,17]
print(solution.findMin(nums))
nums = [5,1,2,3,4]
print(solution.findMin(nums))