from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])

        top, bot = 0 , ROWS - 1
        # binary search to look for the row
        while top <= bot:
            row = (top + bot) // 2
            if target > matrix[row][-1]: # look at rightmost value
                top = row + 1 # look at larger rows
            elif target < matrix[row][0]: # look first value
                bot = row - 1 # look smaller rows
            else:
                break
        
        if not (top <= bot): # no rows have the target value
            return False
        
        row = (top + bot) // 2 # row that may have the value
        l, r = 0, COLS - 1
        # perform binary search in each column of the row
        while l <= r:
            m = (l + r) // 2
            if target > matrix[row][m]:
                l = m + 1
            elif target < matrix[row][m]:
                r = m - 1
            else:
                return True # we found the target
        return False # we never found the target

    # my solution
    # def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
    #     l, r = 0, len(matrix) - 1
    #     while l <= r:
    #         m = (l + r) // 2
    #         inner_last_index = len(matrix[m]) - 1

    #         if matrix[m][0] <= target and matrix[m][inner_last_index] >= target:
    #             left, right = 0, len(matrix[m]) - 1 
    #             while left <= right:
    #                 mid = (left + right) // 2

    #                 if matrix[m][mid] == target:
    #                     return True
    #                 elif matrix[m][mid] < target:
    #                     left = mid + 1
    #                 else:
    #                     right = mid - 1
    #             return False # not in matrix
    #         elif matrix[m][0] > target:
    #             r = m - 1
    #         else:
    #             l = m + 1
    #     return False
    # solution: O(m*log(n))
    # def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
    #     # while left <= right:
    #     #     mid = (left + right) // 2
    #     for i in range(0, len(matrix)):
    #         left, right = 0, len(matrix[i]) - 1 
    #         while left <= right:
    #             mid = (left + right) // 2

    #             if matrix[i][mid] == target:
    #                 return True
    #             elif matrix[i][mid] < target:
    #                 left = mid + 1
    #             else:
    #                 right = mid - 1

    #     return False


solution = Solution()
matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 3
print(solution.searchMatrix(matrix, target))
matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 13
print(solution.searchMatrix(matrix, target))