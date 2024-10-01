from typing import List


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        perm = []  # to store permutations
        # create hashmap
        count = {n: 0 for n in nums}
        # update count
        for n in nums:
            count[n] += 1

        def dfs():
            # base case - lengths are equal
            if len(perm) == len(nums):
                # append a copy of the list
                res.append(perm.copy())
                return
            # go through every number (key)
            for n in count:
                if count[n] > 0: # we have enough values
                    perm.append(n)
                    count[n] -= 1 # decrease count
                    # call recursive function:
                    dfs()
                    # clean up increase count, remove value from perm (go up the tree)
                    count[n] += 1
                    perm.pop()

        # function call
        dfs()
        return res


# test
solution = Solution()
nums = [1, 1, 2]
print(solution.permuteUnique(nums))
