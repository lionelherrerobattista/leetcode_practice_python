from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        # two pointers at each end
        left = 0
        right = len(height) - 1
        # store max height for each section
        left_max = height[left]
        right_max = height[right]
        water_amount = 0

        # loop through the heights
        while left < right:
            # calculate the trapped water at each position
            # min(height[l], height[r]) - height[i]
            if left_max < right_max:  # move the min between 2
                left += 1
                # check if new max
                left_max = max(left_max, height[left])
                # calculate amount of water
                water_amount += left_max - height[left]
            else:
                # same but with right pointer
                right -= 1
                right_max = max(right_max, height[right])
                water_amount += right_max - height[right]

        return water_amount

# Complexity
# Time: O(n) - iterae each element of the array once
# Space: O(1) - no extra data structure


solution = Solution()
height = [0, 2, 0, 3, 1, 0, 1, 3, 2, 1]
result = solution.trap(height)
print(result)
