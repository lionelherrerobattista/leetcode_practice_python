class Solution:
    def climbStairs(self, n: int) -> int:
        # base cases
        if n == 1:
            return 1
        if n == 2:
            return 2

        # dp bottom up
        # create table
        dp = [0] * n
        # initial values, ways to reach 1 step or 2 steps
        dp[0] = 1
        dp[1] = 2

        # calculate for rest n steps
        for i in range(2, n):
            dp[i] = dp[i - 2] + dp[i - 1]  # sum of previous 2 steps

        return dp[n - 1]  # return last index with total ways

# Complexity
# Time: O(n) - One iteration to calculate table's values
# Space: O(n) - table to store values


sol = Solution()
n = 3
print(sol.climbStairs(n))
