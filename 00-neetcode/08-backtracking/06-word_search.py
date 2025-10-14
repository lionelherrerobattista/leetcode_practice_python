from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        path = set()

        # backtrack, check if we should add letter in the right or below
        def backtracking(row, col, i):
            # base cases
            # found word
            if i == len(word):
                return True

            # out of bounds
            if (row < 0 or col < 0) or (row >= ROWS or col >= COLS):
                return False

            # letter not in word
            if word[i] != board[row][col]:
                return False

            # letter already visited
            if (row, col) in path:
                return False

            # found char
            # add path
            path.add((row, col))

            # look at all adjacent positions
            res = (
                backtracking(row + 1, col, i + 1) or
                backtracking(row - 1, col, i + 1) or
                backtracking(row, col + 1, i + 1) or
                backtracking(row, col - 1, i + 1)
            )

            # undo decision
            path.remove((row, col))

            return res

        # check every position in the board
        for row in range(ROWS):
            for col in range(COLS):
                if backtracking(row, col, 0):
                    return True  # found the word

        # word is not present
        return False

# Complexity
# Time: O(n * m * 4^n) - n and m for the board, 4^n choices
