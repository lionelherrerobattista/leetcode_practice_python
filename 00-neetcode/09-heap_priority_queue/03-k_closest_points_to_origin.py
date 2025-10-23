import heapq
from typing import List
from math import sqrt


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # k, num of closest points
        # when min heap == k return ?
        distances = []
        heapq.heapify(distances)
        res = []

        # calc distance of points
        for x, y in points:
            # distance to origin (0,0)
            distance = sqrt((x - 0)**2 + (y - 0)**2)
            # use as max heap and touple (inmmutable):
            # orders by distance first
            heapq.heappush(distances, (-1 * distance, x, y))

            if len(distances) > k:  # pop the largest element
                heapq.heappop(distances)

        # add coord to result
        for distance, x, y in distances:
            res.append([x, y])

        return res

# Complexity
# Time: O(n log k) - go through all elements, push and pop elements
# Space: O(k)


sol = Solution()
points = [[0, 2], [2, 2]]
k = 1
print(sol.kClosest(points, k))
points = [[0, 2], [2, 0], [2, 2]]
k = 2
print(sol.kClosest(points, k))
points = [[3, 3], [5, -1], [-2, 4]]
k = 2
print(sol.kClosest(points, k))
