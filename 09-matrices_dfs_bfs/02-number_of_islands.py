from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0]) # m: height, n: width

        def dfs(i, j):
            # traverse and mark the land as water ("1" to "0")
            if (i < 0 or i >= m or
                j < 0 or j >= n or
                grid[i][j] != '1'):
                return # we don't care about it
            else:
                grid[i][j] = '0' # turn into water
                # check other positions
                dfs(i - 1, j) # up
                dfs(i + 1, j) # down
                dfs(i, j + 1) # right
                dfs(i, j - 1) # left

        num_islands = 0
        # traverse grid from left to right, top to bottom
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    # found an island
                    num_islands += 1
                    # turn island into water:
                    dfs(i, j)

        return num_islands
    
# Complexity
# Time: O(m * n) height * width
# Space: O(m * n)

# Tests:
solution = Solution()
grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
print(solution.numIslands(grid))

grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
print(solution.numIslands(grid))