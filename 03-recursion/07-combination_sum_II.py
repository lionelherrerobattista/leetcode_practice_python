from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        # we sort the candidate array to group repeated nums together
        candidates.sort()

        # index, current comb, total sum
        def backtrack(i: int, cur: List[int], total: int):
            # base cases - valid combination
            if total == target:
                res.append(cur.copy())
                return

            # base case - out of bound
            if total > target or i == len(candidates):
                return

            # case: include candidates[i]
            cur.append(candidates[i])
            # + 1, we are not allowed to reuse
            backtrack(i + 1, cur, total + candidates[i])
            cur.pop()  # undo the append, we don't use the current element

            # case: skip candidates[i] if they are the same
            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1  # continue checking
            backtrack(i + 1, cur, total)

        # call to the function
        backtrack(0, [], 0)
        return res


solution = Solution()
candidates = [10, 1, 2, 7, 6, 1, 5]
target = 8
print(solution.combinationSum2(candidates, target))
