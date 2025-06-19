from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)  # initialize at 1

        # calculate prefixes and store in result array:
        prefix = 1  # default value
        for i in range(len(nums)):
            res[i] = prefix  # save in results
            prefix *= nums[i]

        # calculate postfix and multiply by prefixes stored
        # start from the right
        postfix = 1  # default value
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]

        return res

# complexity
# time: O(n) - loop through each array
# complexity: O(1) - result array doesn't count
