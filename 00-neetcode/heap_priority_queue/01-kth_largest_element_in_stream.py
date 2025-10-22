import heapq
from typing import List


class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        # create min heap size k
        self.k = k
        self.minHeap = nums
        heapq.heapify(self.minHeap)
        # pop > k elements
        while len(self.minHeap) > k:
            heapq.heappop(self.minHeap)

    def add(self, val: int) -> int:
        # add value to the heap
        heapq.heappush(self.minHeap, val)

        # check if we have k elements before popping
        if len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)

        # index 0 element always min
        return self.minHeap[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
