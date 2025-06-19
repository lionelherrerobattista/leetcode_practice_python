from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        # two pointers
        # area: length * height
        # use smallest height between two
        # need to find longest and tallest
        left = 0
        right = len(height) - 1  # max width
        max_area = 0

        # find max height that works
        while left < right:
            # calculate area
            area = (right - left) * min(height[left], height[right])
            max_area = max(area, max_area)

            # move pointer, check max heights (tallest)
            if height[left] > height[right]:
                right -= 1
            else:  # if right taller or if equal
                left += 1

        return max_area

# Complexity
# Time: O(n) - loop through the heights array once
# Space: O(1) - No extra data structure used


sol = Solution()
heights = [1, 7, 2, 5, 4, 7, 3, 6]
result = sol.maxArea(heights)
print(result)
