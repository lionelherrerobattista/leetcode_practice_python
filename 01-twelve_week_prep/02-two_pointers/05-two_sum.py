from typing import List
from collections import defaultdict


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indexes = defaultdict(int)

        # create dict of indexes
        for i, num in enumerate(nums):
            indexes[num] = i

        # iterate search two_sum
        for i, num in enumerate(nums):
            # calculate the other number
            # that we need to form the pair
            value_to_search = target - num

            # check if in dictionary
            # and if the index is different (constraint)
            if value_to_search in indexes and indexes[value_to_search] != i:
                return [i, indexes[value_to_search]]

# Complexity
# Time: O(n)
# Space: O(n)


# TESTS
solution = Solution()
nums = [2, 7, 11, 15]
target = 9
print(solution.twoSum(nums, target))
nums = [3, 2, 4]
target = 6
print(solution.twoSum(nums, target))
nums = [3, 3]
target = 6
print(solution.twoSum(nums, target))
