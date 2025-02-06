from typing import List


class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        result = 0
        product = 1  # neutral value for product (avoid division by 0)
        # two pointer approach
        left = 0

        for right, _ in enumerate(nums):
            # calculate the product
            product *= nums[right]
            # handle invalid value
            while left <= right and product >= k:
                # update product (divide as we are multiplying)
                product = product // nums[left]
                # shift left pointer to make product valid
                left += 1
            # add the size of the subarray
            # distance between pointers defines the amount of subarrays we find
            result += (right - left + 1)

        # return value
        return result

# Complexity
# Time: O(n)
# Space: O(1)


# TEST
solution = Solution()
nums = [10, 5, 2, 6]
k = 100
print(solution.numSubarrayProductLessThanK(nums, k))
nums = [1, 2, 3]
k = 0
print(solution.numSubarrayProductLessThanK(nums, k))
