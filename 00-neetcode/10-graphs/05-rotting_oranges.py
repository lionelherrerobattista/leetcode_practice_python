from typing import List
from collections import deque


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        EMPTY, FRESH, ROTTEN = 0, 1, 2  # grid values
        # grid length:
        rows = len(grid)
        columns = len(grid[0])
        # for BFS
        visited = set()
        banana_queue = deque()
        fresh_count = 0

        # to add to queue
        def add_banana(i, j):
            # check out of bounds
            if i < 0 or j < 0 or i >= rows or j >= columns:
                return

            # empty or rotten
            if grid[i][j] == EMPTY or grid[i][j] == ROTTEN:
                return

            # visited
            if (i, j) in visited:
                return

            # add neighbor
            banana_queue.append((i, j))
            visited.add((i, j))

            # one less fresh
            nonlocal fresh_count
            fresh_count -= 1

        # look for rotten fruits
        for row in range(rows):
            for column in range(columns):
                if grid[row][column] == ROTTEN:
                    # add to queue and visited set
                    banana_queue.append((row, column))
                    visited.add((row, column))
                elif grid[row][column] == FRESH:
                    fresh_count += 1

        # bfs iterative
        minute = 0  # minutes to rot
        while banana_queue:
            # empty queue
            queue_size = len(banana_queue)  # level length
            for _ in range(queue_size):  # level
                row, column = banana_queue.popleft()

                grid[row][column] = 2  # turn rotten

                # check neighbors, and add to queue
                add_banana(row + 1, column)
                add_banana(row - 1, column)
                add_banana(row, column + 1)
                add_banana(row, column - 1)

            if banana_queue:  # avoid last iteration with empty queue
                minute += 1

        # check if any fresh left
        if fresh_count > 0:
            return -1

        return minute

# Complexity
# Time: O(m*n)
# Space: O(m*n)


sol = Solution()
grid = [[1, 1, 0], [0, 1, 1], [0, 1, 2]]
print(sol.orangesRotting(grid))
