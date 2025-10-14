from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        permutations = []  # final result
        cur_permutation = []

        # iterate through decision tree

        def backtrack():
            # base case
            if len(cur_permutation) == len(nums):
                permutations.append(cur_permutation.copy())
                return

            # iterate through the possible nums
            for number in nums:
                # add number only if the number is not in the current permutation
                if number not in cur_permutation:
                    cur_permutation.append(number)
                    backtrack()  # recursive call
                    cur_permutation.pop()  # undo decision

        backtrack()

        return permutations

# Complexity
# Time: O(n!)
# Space: O(n)
