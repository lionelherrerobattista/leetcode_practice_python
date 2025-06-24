from typing import List
import functools

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        for i, n in enumerate(nums):
            nums[i] = str(n) # convert to strings to compare

        # function to compare
        def compare(n1, n2):
            if n1 + n2 > n2 + n1:
                return -1 # n1 goes first
            else:
                return 1 # sort
        # sort the numbers using the function
        nums = sorted(nums, key=functools.cmp_to_key(compare))

        # return a string with largest number
        # special case with 00000, convert to int and str again = 0
        return str(int("".join(nums)))
    
# test
solution = Solution()
nums = [10,2]
print(solution.largestNumber(nums))
nums = [3,30,34,5,9]
print(solution.largestNumber(nums))