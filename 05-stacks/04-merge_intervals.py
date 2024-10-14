from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # sort the input O(n * log n)
        # by the start value
        intervals.sort(key = lambda interval : interval[0])
        output = [intervals[0]] # take first interval

        # iterate through the rest
        # get start and end values
        for start, end in intervals[1:]:
            # get most recently added
            # use the last value
            last_end = output[-1][1]

            # check overlap
            if start <= last_end:
                # replace the last value if greater
                output[-1][1] = max(last_end, end)
            else:
                # non overlapping, add the interval
                output.append([start, end])

        return output


# test
solution = Solution()
intervals = [[1,3],[2,6],[8,10],[15,18]]
print(solution.merge(intervals))
intervals = [[1,4],[4,5]]
print(solution.merge(intervals))
intervals = [[1,3]]
print(solution.merge(intervals))
intervals = [[1,4],[5,6]]
print(solution.merge(intervals))
intervals = [[1,4],[0,4]]
print(solution.merge(intervals))
