from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        # binary seach on first column
        top_row = 0
        bottom_row = len(matrix) - 1

        while top_row <= bottom_row:
            mid_row = top_row + ((bottom_row - top_row) // 2)

            if target > matrix[mid_row][-1]:  # last element of mid row
                top_row = mid_row + 1
            elif target < matrix[mid_row][0]:  # first element of mid row
                bottom_row = mid_row - 1
            else:
                break  # found row

        # check if row wasn't found
        if not (top_row <= bottom_row):
            return False  # target is not in matrix

        mid_row = top_row + ((bottom_row - top_row) // 2)

        # perform binary search in each column of the row
        left = 0
        right = len(matrix[mid_row]) - 1

        while left <= right:
            mid = left + ((right - left) // 2)

            if matrix[mid_row][mid] > target:
                # discard greater part
                right = mid - 1
            elif matrix[mid_row][mid] < target:
                # discar upper part
                left = mid + 1
            else:
                # found target
                return True

        return False  # target is not in matrix

# Complexity
# Time: O(log(m * n)) - Binary search
# Space: O(1)


sol = Solution()
matrix = [[1, 2, 4, 8], [10, 11, 12, 13], [14, 20, 30, 40]]
target = 10
print(sol.searchMatrix(matrix, target))

matrix = [[1]]
target = 1
print(sol.searchMatrix(matrix, target))
