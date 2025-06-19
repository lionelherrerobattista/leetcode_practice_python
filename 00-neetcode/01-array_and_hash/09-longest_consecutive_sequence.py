from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # create set of every number to check if it exists
        nums_set = set(nums)
        longest_sequence = 0

        # check sequence
        for num in nums_set:
            # search for the start of a sequence
            # (if no previous number exist doesn't exist)
            if (num - 1) not in nums_set:
                # start of a sequence
                sequence_count = 1
                while (num + sequence_count) in nums_set:
                    # check sequence
                    # (if next number exist)
                    sequence_count += 1

                # check if longer than max
                longest_sequence = max(sequence_count, longest_sequence)

        return longest_sequence

# complexity
# Time: O(n) - visit each num in array once
# Space: O(n) - use of set


solution = Solution()
nums = [2, 20, 4, 10, 3, 4, 5]
result = solution.longestConsecutive(nums)
print(result)
