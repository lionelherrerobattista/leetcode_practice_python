from typing import List

class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        left, right = 0, len(arr) - 1

        while left <= right:
            mid = (left + right) // 2
            # check left element
            # if the middle is < than left element
            # we should continue searching left
            if mid > 0 and arr[mid] < arr[mid - 1]:
                right = mid - 1 # check left window
            # check right element
            # if the middle is < than right element
            # we should continue searching right
            elif mid < len(arr) - 1 and arr[mid] < arr[mid + 1]:
                left = mid + 1
            else:
                return mid

solution = Solution()
arr = [0,1,0]
print(solution.peakIndexInMountainArray(arr))
arr = [0,2,1,0]
print(solution.peakIndexInMountainArray(arr))
arr = [0,10,5,2]
print(solution.peakIndexInMountainArray(arr))