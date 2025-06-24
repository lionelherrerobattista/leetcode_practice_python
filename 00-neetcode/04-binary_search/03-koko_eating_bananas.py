from typing import List
import math


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # 1 <= target >= max_pile
        # rate: ceil(banana pile / bananas) < h
        # binary search - k_test (yes, or no condition)

        left = 1  # smallest amount possible
        # get max number in piles, every other will take 1 hour
        right = max(piles)  # O(n)
        min_rate = right  # init max rate it will take

        while left <= right:
            mid = left + ((right - left) // 2)

            hours = 0

            # check rate
            for pile in piles:
                hours += math.ceil(pile / mid)

            # check min
            if hours <= h:
                min_rate = min(min_rate, mid)
                # check if there is a smaller rate
                right = mid - 1
            else:
                # rate > h:
                # rate should be greater, not enough time
                left = mid + 1

        return int(min_rate)


sol = Solution()
piles = [1, 4, 3, 2]
h = 9
print(sol.minEatingSpeed(piles, h))
piles = [25, 10, 23, 4]
h = 4
print(sol.minEatingSpeed(piles, h))
