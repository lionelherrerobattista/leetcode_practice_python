from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        result = 0
        # define two pointers
        left = 0
        right = len(height) - 1

        # iterate array
        while left < right:
            # calculate area
            # height: min to avoid slant
            container_height = min(height[left], height[right])
            # witdth: distance between two pointers
            container_width = right - left

            # check area
            area = container_height * container_width
            result = max(result, area)

            # move pointers
            # peek next (?)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return result

# Complexity
# Time: O(n)
# Space: O(1)


# test
solution = Solution()
height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
print(solution.maxArea(height))
height = [1, 1]
print(solution.maxArea(height))
height = [1, 2, 4, 3]
print(solution.maxArea(height))
