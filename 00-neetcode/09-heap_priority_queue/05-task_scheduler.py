import heapq
from typing import List
from collections import defaultdict, deque


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # n = cycles to separate identical tasks
        max_heap = []
        task_frequency = defaultdict(int)
        task_queue = deque()
        time = 0  # track processing time

        heapq.heapify(max_heap)

        # calculate frequency of tasks
        for task in tasks:
            task_frequency[task] += 1

        # order more frequent to least, max heap
        for task, frequency in task_frequency.items():
            heapq.heappush(max_heap, -1 * frequency)

        while max_heap or task_queue:
            time += 1

            if max_heap:
                frequency = heapq.heappop(max_heap)
                count = 1 + frequency  # one less task, frequency is negative

                if count:  # if there are still tasks
                    # calculate time to be available again
                    task_queue.append((count, time + n))

            if task_queue:
                # get the next task in the queue
                task_count, task_time = task_queue[0]
                if task_time == time:
                    task_count, task_time = task_queue.popleft()
                    heapq.heappush(max_heap, task_count)

        return time


sol = Solution()
tasks = ["X", "X", "Y", "Y"]
n = 2
print(sol.leastInterval(tasks, n))
