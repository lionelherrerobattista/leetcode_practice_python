from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()  # to eliminate duplicates

        for i, a in enumerate(nums):
            # avoid using the same value twice
            if i > 0 and a == nums[i - 1]:
                continue

            # create pointers
            left, right = i + 1, len(nums) - 1

            while left < right:
                # calculate 3sum
                threeSum = a + nums[left] + nums[right]

                # shift pointers
                if threeSum > 0:
                    # make 3sum smaller
                    right -= 1
                elif threeSum < 0:
                    # make 3sum bigger
                    left += 1
                else:
                    # we have the result
                    result.append([a, nums[left], nums[right]])
                    left += 1
                    # check if same value
                    while nums[left] == nums[left - 1] and left < right:
                        # keep updating the pointer
                        left += 1
                    # right pointer will also update with the conditions above

        return result

# Complexity
# Time: O(n^2)
# Space: O(n)


# TEST
solution = Solution()
nums = [-1, 0, 1, 2, -1, -4]
print(solution.threeSum(nums))
