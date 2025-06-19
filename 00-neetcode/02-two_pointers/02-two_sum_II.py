from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # non-drecreasing = lowest to highest
        # two pointers
        left = 0
        right = len(numbers) - 1

        while left < right:
            aux_sum = numbers[left] + numbers[right]
            if aux_sum == target:
                return [left + 1, right + 1]  # 1-indexed
            # else move pointers
            elif aux_sum > target:
                right -= 1  # make sum smaller
            else:
                left += 1  # make sum bigger

        return []

# Complexity
# Time: O(n) - loop through each element once
# Space: O(1) - No extra memory


numbers = [1, 2, 3, 4]
target = 3
solution = Solution()
result = solution.twoSum(numbers, target)
print(result)
numbers = [1, 5, 9, 10]
target = 11
result = solution.twoSum(numbers, target)
print(result)
numbers = [-5, -3, 0, 2, 4, 6, 8]
target = 5
result = solution.twoSum(numbers, target)
print(result)
