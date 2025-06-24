from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)  # 0 if no greater temp
        temp_indexes = []  # store indexes, monotonic stack

        for index, temp in enumerate(temperatures):
            # compare temp, with stack
            while temp_indexes and temp > temperatures[temp_indexes[-1]]:
                # found warmer temp
                days_difference = index - temp_indexes[-1]
                result[temp_indexes[-1]] = days_difference  # calculate days
                temp_indexes.pop()  # remove the temp
            # not warmer
            temp_indexes.append(index)

        return result

# Complexity:
# Time: O(n) - visit each element of the temp array once
# Space: O(n) - use of a monotonic stack to store indexes


temperatures = [30, 38, 30, 36, 35, 40, 28]
sol = Solution()
print(sol.dailyTemperatures(temperatures))
