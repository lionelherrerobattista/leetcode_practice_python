from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # create table
        cost_length = len(cost)
        dp = [0] * (cost_length + 1)  # +1 to escape the array

        # 2 initial values already set, cost 0

        # calculate all remaining costs
        for i in range(2, cost_length + 1):
            dp[i] = min(cost[i - 2] + dp[i - 2], cost[i - 1] + dp[i - 1])

        # last value, is the min cost
        return dp[cost_length]

# Complexity
# Time: O(n) - check every cost 1 time
# Space: O(n) - dp array


sol = Solution()
cost = [1, 2, 1, 2, 1, 1, 1]
print(sol.minCostClimbingStairs(cost))
