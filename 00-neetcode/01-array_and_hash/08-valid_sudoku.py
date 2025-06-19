from collections import defaultdict
from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # 3 hashsets
        # set will contain a num set for each col, row or square
        cols_hash = defaultdict(set)
        rows_hash = defaultdict(set)
        squares_hash = defaultdict(set)

        # check board's rows and columns
        # sudoku 9 x 9
        for row in range(9):
            for column in range(9):
                num = board[row][column]
                # check for empty space
                if num == ".":
                    continue

                # check if num is in any hash
                # square is 3 * 3, check square with row // 3, column // 3
                if (num in rows_hash[row]
                    or num in cols_hash[column]
                        or num in squares_hash[row // 3, column // 3]):
                    return False  # not valid

                # add num to sets
                cols_hash[column].add(num)
                rows_hash[row].add(num)
                squares_hash[row // 3, column // 3].add(num)

        return True  # is valid

# Complexity
# Time: O(n^2) - we go through every row and column
# Comlexity: O(n) - use of hash sets


solution = Solution()
board = [["1", "2", ".", ".", "3", ".", ".", ".", "."],
         ["4", ".", ".", "5", ".", ".", ".", ".", "."],
         [".", "9", "8", ".", ".", ".", ".", ".", "3"],
         ["5", ".", ".", ".", "6", ".", ".", ".", "4"],
         [".", ".", ".", "8", ".", "3", ".", ".", "5"],
         ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
         [".", ".", ".", ".", ".", ".", "2", ".", "."],
         [".", ".", ".", "4", "1", "9", ".", ".", "8"],
         [".", ".", ".", ".", "8", ".", ".", "7", "9"]]

result = solution.isValidSudoku(board)

print(result)
