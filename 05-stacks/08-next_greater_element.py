from typing import List

class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stack = []
        answer = [-1] * len(nums)
        # check element on the right
        for i, num in enumerate(nums):
            # we check the value of element in stack
            while stack and stack[-1][0] < num:
                # if we found a greater num
                # we pop the element and update the answer at index
                answer[stack[-1][1]] = num
                stack.pop()
            stack.append((num, i))
        # check remaining elements (circular array)
        for i, num in enumerate(nums):
            # we check the value of element in stack
            while stack and stack[-1][0] < num:
                # if we found a greater num
                # we pop the element and update the answer at index
                answer[stack[-1][1]] = num
                stack.pop()
            stack.append((num, i))
        return answer

# test
solution = Solution()
nums = [1,2,1]
print(solution.nextGreaterElements(nums))