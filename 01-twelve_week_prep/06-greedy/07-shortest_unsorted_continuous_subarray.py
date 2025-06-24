from typing import List

class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        if len(nums) < 2: # edge case, no sorting
            return 0
        
        max_value = nums[0]
        end = 0
        # find largest index not in place
        # end of subarray
        for i in range(0, len(nums)):
            if nums[i] < max_value:
                end = i # keep index of subarray
            else:
                max_value = nums[i] # it's ordered
        
        min_value = nums[-1]
        start = len(nums) - 1
        # find the smallest index not in place
        # beginning of sub array
        # start from the end
        for i in range(len(nums)-1, -1, -1):
            if nums[i] > min_value:
                start = i # not ordered
            else:
                min_value = nums[i] # decreasing order

        if end != 0:
            return end - start + 1 # calculate distance between indexes
        else:
            return 0 # no need to sort





        # solution with two pointers, not passing all tests
    # def findUnsortedSubarray(self, nums: List[int]) -> int:
        # l, r = 0, len(nums) - 1
        # start_index = 0
        # end_index = 0

        # # edge case, whole array decreasing ?
        # if nums[l] > nums[r]:
        #     return len(nums)

        # while l <= r:
        #     # check left index
        #     if l < len(nums) - 1 and nums[l] > nums[l + 1]: # compare to next
        #         start_index = l # sub array starts at l
            
        #     if r > 0 and nums[r] < nums[r - 1]: # compare to previous
        #         end_index = r # found end of subarray

        #     l += 1
        #     r -= 1
        # # check sub array
        # if start_index != end_index:
        #     return len(nums[start_index:end_index + 1])
        # else:
        #     return 0

            
solution = Solution()
nums = [2,6,4,8,10,9,15]
print(solution.findUnsortedSubarray(nums))
nums = [5,4,3,2,1]
print(solution.findUnsortedSubarray(nums))
nums = [1,3,2,4,5]
print(solution.findUnsortedSubarray(nums))
nums = [1,2,3,3,3]
print(solution.findUnsortedSubarray(nums))
nums = [1,3,2,2,2]
print(solution.findUnsortedSubarray(nums))