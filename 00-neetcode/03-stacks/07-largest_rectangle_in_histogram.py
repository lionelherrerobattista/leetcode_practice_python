from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0
        stack = []  # pair: (index, height)

        # check each height
        for i, h in enumerate(heights):
            rectangle_start = i  # rectangle start
            # pop elements from stack if they are greater
            # can't extend it to the right
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                # calculate area
                max_area = max(max_area, height * (i - index))
                rectangle_start = index
            # add the current height to the stack
            stack.append((rectangle_start, h))

        # check if remaining height in stack
        # they reach the end of the histogram len(heights)
        for i, h in stack:
            max_area = max(max_area, h * (len(heights) - i))

        return max_area


sol = Solution()
heights = [7, 1, 7, 2, 2, 4]
print(sol.largestRectangleArea(heights))
