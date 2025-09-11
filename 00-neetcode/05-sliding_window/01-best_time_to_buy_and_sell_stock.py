from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0  # init profit

        if len(prices) == 1:  # edge case
            return max_profit  # no profit

        # two pointers
        left = 0  # buy
        right = 1  # sell

        # move pointers
        while right < len(prices):
            buy_price = prices[left]
            sell_price = prices[right]

            if buy_price < sell_price:  # check if profitable
                profit = sell_price - buy_price
                # check if new max
                max_profit = max(profit, max_profit)
            else:
                left = right  # we want the left always at min

            right += 1  # always check future price
        return max_profit

# Complexity
# Time: O(n) - iterate array 1 time
# Space: O(1) - No extra space


sol = Solution()
prices = [10, 1, 5, 6, 7, 1]
print(sol.maxProfit(prices))

prices = [10, 8, 7, 5, 2]
print(sol.maxProfit(prices))

prices = [2, 1, 2, 1, 0, 1, 2]
print(sol.maxProfit(prices))
