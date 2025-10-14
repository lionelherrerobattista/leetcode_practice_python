from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        combination = []
        combination_list = []

        # sort to detect duplicate combinations
        candidates.sort()

        def backtracking(i, current_sum):
            # base cases
            if current_sum == target:  # found result
                combination_list.append(combination.copy())
                return

            if i >= len(candidates) or current_sum > target:
                # out of bounds or exceeded target
                return

            # decisions
            # choose number
            current_candidate = candidates[i]
            combination.append(current_candidate)

            # i + 1, don't reuse candidate
            backtracking(i + 1, current_sum + current_candidate)

            # undo decision
            combination.pop()

            # don't choose number
            # shift i to avoid duplicates
            # if 1,1,.. we don't want to include neither of those 1s
            while i < len(candidates) and current_candidate == candidates[i]:
                i += 1

            backtracking(i, current_sum)

        backtracking(i=0, current_sum=0)

        return combination_list

# Complexity
# Time: 2^n
# Space: O(h)
