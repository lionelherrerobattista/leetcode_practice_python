from typing import List
import heapq


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        min_heap = []  # will keep the k smallest elements, first is k in sorted order
        heapq.heapify(min_heap)

        for n in nums:
            # add next element
            heapq.heappush(min_heap, n)

            # keep the heap size below k
            if len(min_heap) > k:
                heapq.heappop(min_heap)

        return min_heap[0]  # return first == kth

# Complexity
# Time: O(n log k) - heap inserts element in O(n) time, orders in O(log k)
# Space: O(k) - heap


sol = Solution()
nums = [2, 3, 1, 5, 4]
k = 2
print(sol.findKthLargest(nums, k))
nums = [3, 2, 3, 1, 2, 4, 5, 5, 6]
k = 4
print(sol.findKthLargest(nums, k))
