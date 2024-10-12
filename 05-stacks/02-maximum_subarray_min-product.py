from typing import List

class Solution:
    def maxSumMinProduct(self, nums: List[int]) -> int:
        res = 0
        stack = []
        # we have the prefix of any subarray
        # to compute the sum in O(n) time
        prefix = [0]

        # calculate sums
        for n in nums:
            # to the last value of the prefix array
            # we add the current value
            prefix.append(prefix[-1] + n)

        for i, n in enumerate(nums):
            new_start = i
            # check top value in stack (index, value)
            while stack and stack[-1][1] > n:
                # pop the value to keep in monotonic increasing order
                start, val = stack.pop()
                # compute min-product
                # we use the prefix (sum up until that value in i)
                total = prefix[i] - prefix[start]
                res = max(res, val * total) # check if max
                # update the start value for n
                # it will replace the value we popped
                new_start = start
            # add the value to the stack
            stack.append((new_start,n))
        # check remaining values in stack
        for start, val in stack:
            # compute the biggest subarray
            # end index should be length of the entire array
            total = prefix[len(nums)] - prefix[start]
            res = max(res, val * total)
        # return the result modded bythe value provided
        return res % (10**9 + 7)

# test
solution = Solution()
nums = [1,2,3,2]
print(solution.maxSumMinProduct(nums))
nums = [2,3,3,1,2]
print(solution.maxSumMinProduct(nums))
nums = [3,1,5,6,4,2]
print(solution.maxSumMinProduct(nums))