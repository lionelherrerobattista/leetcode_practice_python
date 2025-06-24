from typing import List
from collections import deque


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        result = []
        nums_queue = deque()  # contains index
        start, end = 0, 0

        # slide window
        while end < len(nums):
            # remove the smaller values from queue
            while nums_queue and nums[nums_queue[-1]] < nums[end]:
                nums_queue.pop()
            # append index to the queue
            nums_queue.append(end)

            # shift window
            # remove left index from window
            # index is already out of bounds
            if start > nums_queue[0]:
                nums_queue.popleft()

            # update output if window is at least k
            # avoid adding the first numbers to output
            # move left pointer
            if (end + 1) >= k:
                result.append(nums[nums_queue[0]])
                start += 1

            # increment window, move right pointer
            end += 1

        return result

# Complexity
# Time: O(n)
# Space: O(n)


# TEST
solution = Solution()
nums = [1, 3, -1, -3, 5, 3, 6, 7]
k = 3
print(solution.maxSlidingWindow(nums, k))
nums = [1]
k = 1
print(solution.maxSlidingWindow(nums, k))
