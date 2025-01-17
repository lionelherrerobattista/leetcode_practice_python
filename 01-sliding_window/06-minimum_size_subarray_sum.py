from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        min_length = float('inf')
        sub_array_sum = 0
        start = 0

        # two pointers
        # move right pointer while sum is < target
        for end in range(len(nums)):
            sub_array_sum += nums[end]

            # check the length,
            # move left pointer while sum is greater
            # or equal than target
            while sub_array_sum >= target:
                min_length = min(min_length, end - start + 1)
                sub_array_sum -= nums[start]
                start += 1

        if min_length == float('inf'):
            return 0  # no sub array was found

        return min_length


solution = Solution()
target = 7
nums = [2, 3, 1, 2, 4, 3]
print(solution.minSubArrayLen(target, nums))
target = 4
nums = [1, 4, 4]
print(solution.minSubArrayLen(target, nums))
target = 11
nums = [1, 1, 1, 1, 1, 1, 1, 1]
print(solution.minSubArrayLen(target, nums))
