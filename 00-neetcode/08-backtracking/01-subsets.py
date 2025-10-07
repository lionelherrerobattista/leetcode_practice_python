from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subset_list = []
        subset = []

        def backtrack(index):
            # base case - last level
            if index == len(nums):
                subset_list.append(subset.copy())  # append to final list
                return

            # Explore paths:
            # Pick number
            subset.append(nums[index])
            backtrack(index + 1)

            # Don't pick number
            subset.pop()
            backtrack(index + 1)

        # execute function, start at index 0
        backtrack(0)

        return subset_list


# Complexity
# Time: O(2^n) - Doubleing the number of solutions with each level
# Space: O(h) - Hight of the call stack

sol = Solution()
nums = [1, 2, 3]

print(sol.subsets(nums))
