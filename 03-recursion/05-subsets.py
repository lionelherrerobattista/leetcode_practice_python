from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        subset = []

        def dfs(i: int):  # i => index of the current element
            # base case, out of bounds, reached the leaf node
            if i >= len(nums):
                # we add a copy of the leaf node
                res.append(subset.copy())
                return

            # make decisions:
            # decision to include nums[i] -current value-
            subset.append(nums[i])
            dfs(i + 1)

            # decision NOT to include nums[i] -current value-
            subset.pop()
            dfs(i + 1)

        # function call
        dfs(0)
        return res


solution = Solution()
nums = [1, 2, 3]
print(solution.subsets(nums))
nums = [0]
print(solution.subsets(nums))
