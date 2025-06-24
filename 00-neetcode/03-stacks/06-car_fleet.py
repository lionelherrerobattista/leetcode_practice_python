from typing import List


class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = [(position[i], speed[i])
                 for i in range(len(position))]  # list comprehension
        fleets = 0  # keep track of fleets that arrive
        cur_time = 0  # keep track of time in the road

        # check the pairs, how long they take to reach target?
        for dist, sp in sorted(pairs, reverse=True):  # sort in reverse order
            destination_time = (target - dist) / sp  # calculate time

            if cur_time < destination_time:
                # they merge into a single fleet (travel at the same speed)
                fleets += 1
                cur_time = destination_time

        return fleets

# Complexity:
# Time: O(n log n) - Iterate over a sorted array
# Space: O(n) - Create extra array
