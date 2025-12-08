from collections import defaultdict
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # bucket sort
        count = defaultdict(int)
        # define bucket: index:frequency, value:element[]
        # frequency won't be bigger than len of nums
        freq = [[] for i in range(len(nums) + 1)]

        # save the frequency of each value
        for num in nums:
            count[num] += 1

        # save count in bucket
        for num, cnt in count.items():
            freq[cnt].append(num)

        # loop array backwards and return k elements
        res = []
        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    # already found all k elements
                    return res

# Complexity
# Time: O(n) - loop all elements
# Complexity: O(n) - use of dictionary and array, but size n


solution = Solution()
nums = [1, 2, 2, 3, 3, 3]
k = 2
result = solution.topKFrequent(nums, k)
print(result)
