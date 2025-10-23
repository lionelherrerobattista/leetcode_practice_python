import heapq
from typing import List


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        # convert to negative, to make max heap
        max_heap = [-1 * s for s in stones]
        heapq.heapify(max_heap)  # turn into max heap, ordered desc

        while len(max_heap) > 1:
            first_largest = -1 * heapq.heappop(max_heap)  # convert back
            second_largest = -1 * heapq.heappop(max_heap)

            if first_largest == second_largest:
                # both destroyed
                continue

            # smash both
            new_stone = first_largest - second_largest
            heapq.heappush(max_heap, -1 * new_stone)

        if not max_heap:
            return 0

        return -1 * heapq.heappop(max_heap)  # return last stone

# Complexity
# Time: O(n log n) - n = reorder heap, log n = push element
# Space: O(1)


sol = Solution()
stones = [2, 3, 6, 2, 4]
print(sol.lastStoneWeight(stones))
stones = [2, 2]
print(sol.lastStoneWeight(stones))
