from typing import List

class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        stack = [] # (int, min_value_left), mono decreasing
        current_min = nums[0]

        #iterate array
        for n in nums[1:]:
            # check if we have a min value in stack
            while stack and n >= stack[-1][0]: 
                stack.pop()
            # check pattern, value in stack and min_value
            # n < stack[-1][0] we can avoid using n < stack[-1][0]
            if stack and n < stack[-1][0] and n > stack[-1][1]:
                return True
            # append the value
            stack.append((n, current_min))
            # update current min
            current_min = min(current_min, n)
        return False
        
    
solution = Solution()
nums = [1,2,3,4]
print(solution.find132pattern(nums))
nums = [3,1,4,2]
print(solution.find132pattern(nums))
nums = [-1,3,2,0]
print(solution.find132pattern(nums))