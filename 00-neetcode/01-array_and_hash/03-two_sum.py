from typing import List
from collections import defaultdict


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # create hashmap with numbers and index
        nums_hash = defaultdict(int)

        # load the num as key and index as value
        for i, num in enumerate(nums):
            nums_hash[num] = i

        # loop nums array
        for i in range(0, len(nums)):
            # find the missing number to reach target
            aux = target - nums[i]

            # check if it is in the array
            # and if it is different than i
            if aux in nums_hash and i != nums_hash[aux]:
                j = nums_hash[aux]
                return [i, j]

        return [0, 0]


# Complexity
# Time: O(n) - iterate once
# Space: O(n) - create a hashmap
