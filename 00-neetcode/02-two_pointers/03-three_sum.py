from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []  # store triplets

        # sort array
        nums.sort()

        for i, num in enumerate(nums):  # three pointers
            if i > 0 and num == nums[i - 1]:
                continue
            # have one number, two sum for the other two
            left = i + 1
            right = len(nums) - 1
            while left < right:
                aux_sum = nums[i] + nums[left] + nums[right]

                # check sum
                if aux_sum == 0:  # append triplet
                    res.append(
                        [nums[i], nums[left], nums[right]])
                    left += 1  # continue checking
                    # shift again if the value is the same
                    while nums[left] == nums[left - 1] and left < right:
                        left += 1
                # else, increase or decrease sum
                elif aux_sum > 0:
                    right -= 1  # decrement sum
                else:
                    left += 1

        return res

# Complexity
# Time: O(n^2) - loop twice through the list
# Space: O(m) - space of the triplets returned


nums = [-1, 0, 1, 2, -1, -4]
solution = Solution()
result = solution.threeSum(nums)
print(result)
