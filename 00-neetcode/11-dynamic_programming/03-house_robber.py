from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        houses_length = len(nums)

        if houses_length == 1:
            return nums[0]
        elif houses_length == 2:
            return max(nums[0], nums[1])

        # create table, bottom up DP (tabulation)
        dp = [0] * houses_length

        # base cases
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        for i in range(2, houses_length):
            # calculate choices
            # take house's money and two houses back
            rob_house = nums[i] + dp[i - 2]
            not_rob_house = dp[i - 1]  # keep previous amount

            dp[i] = max(rob_house, not_rob_house)  # get the best choice

        return dp[houses_length - 1]


nums = [1, 1, 3, 3]
sol = Solution()
print(sol.rob(nums))
