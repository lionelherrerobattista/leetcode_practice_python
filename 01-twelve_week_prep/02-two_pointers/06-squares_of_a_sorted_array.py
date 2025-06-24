from typing import List


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        # create array
        result = []
        # two pointers
        # leftmost and rightmost ends of the array
        left = 0
        right = len(nums) - 1

        while left <= right:
            # append biggest numbers
            # compare absolute value
            if abs(nums[left]) > abs(nums[right]):
                result.append(nums[left] ** 2)  # append squared
                # move left pointer
                left += 1
            else:
                result.append(nums[right] ** 2)  # append squared
                # move right pointer
                right -= 1

        # reverse the array
        # it is originally built in desc order
        result.reverse()

        return result

# Complexity
# Time: O(n)
# Space: O(n)/O(1)


# TEST
solution = Solution()
nums = [-4, -1, 0, 3, 10]
print(solution.sortedSquares(nums))
nums = [-7, -3, 2, 3, 11]
print(solution.sortedSquares(nums))
