from typing import List

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1 # initialize pointers

        # binary search
        while l <= r:
            # calculate middle point
            # r - l, guarantee no overflow
            m = l + ((r - l) // 2)
            #check if left neighbor greater
            # and if not 0, avoid index out of bounds
            if m > 0 and nums[m] < nums[m - 1]:
                # continue checking left side
                r = m - 1
            #check if right neighbor greater
            # and if not last element, avoid index out of bounds
            elif m < len(nums) - 1 and nums[m] < nums[m + 1]:
                # continue checking right side
                l = m + 1
            else:
                # we found the peak element
                return m

# tests
solution = Solution()
nums = [1,2,3,1]
print(solution.findPeakElement(nums))
nums = [1,2,1,3,5,6,4]
print(solution.findPeakElement(nums))