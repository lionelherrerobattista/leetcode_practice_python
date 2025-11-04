from typing import List
from collections import deque


class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        # bounds
        rows = len(grid)
        columns = len(grid[0])
        # iterative bfs
        visited = set()
        queue = deque()

        def add_room(i, j):
            if i < 0 or j < 0 or i >= rows or j >= columns:  # out of bounds
                return

            if grid[i][j] == -1:  # can't be traversed
                return

            if (i, j) in visited:  # already visited
                return

            visited.add((i, j))
            queue.append((i, j))

        # search for the gates
        for row in range(rows):
            for column in range(columns):
                if grid[row][column] == 0:
                    # add gate location to queue
                    queue.append((row, column))
                    visited.add((row, column))

        # start bfs
        distance = 0  # initial distance
        while queue:
            for _ in range(len(queue)):
                row, column = queue.popleft()
                grid[row][column] = distance
                # check neighbors
                add_room(row + 1, column)
                add_room(row - 1, column)
                add_room(row, column + 1)
                add_room(row, column - 1)
            # increase distance from gate
            distance += 1

# Complexity
# Time: O(m * n)
# Space: O(m * n)


sol = Solution()
grid = [
    [2147483647, -1, 0, 2147483647],
    [2147483647, 2147483647, 2147483647, -1],
    [2147483647, -1, 2147483647, -1],
    [0, -1, 2147483647, 2147483647]
]  # modify in place
sol.islandsAndTreasure(grid)
print(grid)
