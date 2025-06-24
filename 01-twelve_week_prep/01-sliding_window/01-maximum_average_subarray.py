from typing import List

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        current_sum = 0
        start = 0 # left pointer
        max_average = 0
        current_average = 0

        # build window
        for i in range(k):
            current_sum += nums[i]

        # calculate average 
        max_average = current_sum / k
        end = k # right pointer

        # move the window
        while(end < len(nums)):
            # remove start
            current_sum -= nums[start]
            # move start
            start += 1
            # add enf
            current_sum += nums[end]
            # move end
            end += 1

            # check average
            current_average = current_sum / k
            if current_average > max_average:
                max_average = current_average

        return max_average

# test
nums = [1,12,-5,-6,50,3]
k = 4
solution = Solution()
print(solution.findMaxAverage(nums, k))
nums = [5]
k = 1
print(solution.findMaxAverage(nums, k))
