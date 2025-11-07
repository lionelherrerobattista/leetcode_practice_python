from typing import List


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # get the limits
        ROWS = len(heights)
        COLUMNS = len(heights[0])
        # visited sets
        visited_pacific = set()
        visited_atlantic = set()

        def dfs(row, column, visited, prev_height):
            # check base cases
            # out of bounds
            if row < 0 or column < 0 or row >= ROWS or column >= COLUMNS:
                return

            # the values is less, water can't flow
            if heights[row][column] < prev_height:
                return

            # already visited
            if (row, column) in visited:
                return

            # process cell, add to visited
            visited.add((row, column))

            # check all directions, recursively
            dfs(row + 1, column, visited, heights[row][column])
            dfs(row - 1, column, visited, heights[row][column])
            dfs(row, column + 1, visited, heights[row][column])
            dfs(row, column - 1, visited, heights[row][column])

        # check top and bottom limits
        for column in range(COLUMNS):
            # check top row (pacific ocean)
            dfs(0, column, visited_pacific, heights[0][column])
            # check bottom row (atlantic ocean)
            dfs(ROWS - 1, column, visited_atlantic, heights[ROWS - 1][column])

        # check left and right limits
        for row in range(ROWS):
            # check left column (pacific ocean)
            dfs(row, 0, visited_pacific, heights[row][0])
            # check left column (atlantic ocean)
            dfs(row, COLUMNS - 1, visited_atlantic, heights[row][COLUMNS - 1])

        # return the intersection between sets (coords in both)
        return list(visited_pacific & visited_atlantic)


sol = Solution()
heights = [[1, 2, 2, 3, 5], [3, 2, 3, 4, 4], [
    2, 4, 5, 3, 1], [6, 7, 1, 4, 5], [5, 1, 1, 2, 4]]
print(sol.pacificAtlantic(heights))
