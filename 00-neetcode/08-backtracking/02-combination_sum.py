from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # decision tree
        # dfs - explore all possible combinations
        combination_sums = []
        combination = []

        # recursive
        def backtrack(i, curr_sum):
            # base cases
            # 1- found the sum
            if sum(combination) == target:
                # add it to the result
                combination_sums.append(combination.copy())
                return
            # 2- if we explore all the numbers i == length of nums
            # 3- if the sum is > target
            if i == len(candidates) or sum(combination) >= target:
                return

            # add number
            combination.append(candidates[i])
            # explore possibility with multiple instances of num
            backtrack(i, curr_sum + candidates[i])

            # don't add number anymore (avoid duplicates)
            combination.pop()  # undo decision
            backtrack(i + 1, curr_sum)  # try next num

        backtrack(0, 0)  # index = 0, sum = 0

        return combination_sums


sol = Solution()
candidates = [2, 5, 6, 9]
target = 9

print(sol.combinationSum(candidates, target))
