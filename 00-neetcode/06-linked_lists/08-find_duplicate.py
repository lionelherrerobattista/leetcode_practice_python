from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # fast and sow pointers,
        # consider each value as indexes
        slow = 0
        fast = 0

        # find first intersection to detect cycle
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]

            if slow == fast:
                break

        # create a second slow pointer
        # when the 2 slow meet, beginning of cycle
        slow2 = 0
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow == slow2:
                return slow

# Complexity
# Time: O(n)
# Space: O(1)


sol = Solution()
nums = [1, 2, 3, 2, 2]
print(sol.findDuplicate(nums))
