from typing import List


class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # create hashset
        nums_set = set()

        for num in nums:
            if num in nums_set:  # check if in set, constant time
                return True
            # add to set
            nums_set.add(num)

        return False


# Complexity
# Time: O(n) - visit each element once, check hashset in constant time.
# Space: O(n) - use of hashset
