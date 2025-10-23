from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # save limits
        total_rows = len(grid)
        total_columns = len(grid[0])
        island_count = 0

        def dfs(i, j):
            # base cases
            # if out of bounds
            if (i >= total_rows
                    or j >= total_columns
                    or i < 0
                    or j < 0):
                return

            # if 0
            if grid[i][j] == "0":
                return

            grid[i][j] = "0"  # mark as visited, avoid cycles

            # traverse all directions
            dfs(i + 1, j)  # up
            dfs(i - 1, j)  # down
            dfs(i, j + 1)  # right
            dfs(i, j - 1)  # left

        # loop to traverse the grid
        for i in range(total_rows):
            for j in range(total_columns):
                # check if it's an island
                if grid[i][j] == "1":
                    island_count += 1
                    # mark the neighbors
                    dfs(i, j)

        return island_count

# Complexity
# Time: O(m * n) - rows * column
# Space: O(m * n) - length of call stack


sol = Solution()
grid = [
       ["0", "1", "1", "1", "0"],
       ["0", "1", "0", "1", "0"],
       ["1", "1", "0", "0", "0"],
       ["0", "0", "0", "0", "0"]
]
print(sol.numIslands(grid))
