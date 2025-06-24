from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        # sort nums array
        nums.sort()
        closest_sum = float('inf')

        # Create first pointer to iterate nums
        for i, _ in enumerate(nums):
            # avoid using the same number
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # create other 2 pointers to iterate "subarray"
            left = i + 1
            right = len(nums) - 1

            # Use two pointer, to find other 2 integers
            while left < right:
                # calculate 3sum
                three_sum = nums[i] + nums[left] + nums[right]

                # compare distances
                if abs(three_sum - target) < abs(closest_sum - target):
                    closest_sum = three_sum

                # check if we've found target
                if three_sum == target:
                    return three_sum  # there is no better sum
                # else shift pointers
                elif three_sum < target:
                    # increase sum
                    left += 1
                else:
                    # decrease sum
                    right -= 1

        return closest_sum

# Complexity
# Time: O(n^2)
# Complexity: O(n)


# TEST
solution = Solution()
nums = [-1, 2, 1, -4]
target = 1
print(solution.threeSumClosest(nums, target))
nums = [0, 0, 0]
target = 1
print(solution.threeSumClosest(nums, target))
