from typing import List


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        subset_list = []
        subset = []

        # order nums
        # avoid repetition of subsets
        nums.sort()

        def backtracking(i):
            # base case
            if i >= len(nums):
                # copy, avoid modifying original array
                subset_list.append(subset.copy())
                return

            # choice
            # append number
            subset.append(nums[i])
            backtracking(i + 1)

            # undo choice
            subset.pop()

            # check that num is not repeated (avoid duplicates)
            # keep it in-bounds
            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1
            # don't include number
            backtracking(i + 1)

        backtracking(0)  # start at index 0

        return subset_list

# Complexity
# Time: O(n * 2^n) - Sort and tree traversal?
# Space: O(2^n) - store subsets in array
