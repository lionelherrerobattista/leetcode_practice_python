from typing import List


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # define max length
        total_rows = len(grid)
        total_columns = len(grid[0])
        island_max_area = 0

        # dfs to check the island area
        def dfs(i, j):  # rows, col
            # base cases
            # out of bounds
            if i < 0 or j < 0 or i >= total_rows or j >= total_columns:
                return 0

            # check if water tile
            if grid[i][j] == 0:
                return 0

            # else is an island
            # replace by 0, mark as visited
            grid[i][j] = 0

            # check neighbors, + 1 for current tile
            return (1 + dfs(i + 1, j)  # up
                    + dfs(i - 1, j)  # down
                    + dfs(i, j + 1)  # right
                    + dfs(i, j - 1)  # left
                    )

        # check all positions in the grid
        for row in range(total_rows):
            for column in range(total_columns):
                # check if island
                if grid[row][column] == 1:
                    current_island_area = dfs(row, column)
                    # check max
                    island_max_area = max(island_max_area, current_island_area)

        return island_max_area

# Complexity
# Time: O(n * m) - visit all tiles in the grid
# Space: O(n * m) - length of call stack


sol = Solution()
grid = [
    [0, 1, 1, 0, 1],
    [1, 0, 1, 0, 1],
    [0, 1, 1, 0, 1],
    [0, 1, 0, 0, 1]
]
print(sol.maxAreaOfIsland(grid))
