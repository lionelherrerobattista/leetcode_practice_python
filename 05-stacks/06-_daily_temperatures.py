from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        answer = [0] * n # initialize the array at 0
        stack = []

        for i, current_temp in enumerate(temperatures):
            # we iterate while we have elements in the stack
            # and the value at the top is less than the current temperature
            while stack and stack[-1][0] < current_temp:
                # we pop the temp and index from the stack
                stack_temp, stack_temp_index = stack.pop()
                # save the distance between temps
                answer[stack_temp_index] = i - stack_temp_index
            # save the current temp and index to compare
            stack.append((current_temp, i))
        
        return answer
    
    # brute force, TLE:
    # def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
    #     res = []
    #     no_greater_temp = True
    #     
    #     # check every single temp
    #     for i, current_temp in enumerate(temperatures):
    #         # compare current with next
    #         for j, next_temp in enumerate(temperatures[i+1:], start=i+1):
    #             # if next greater, count days
    #             if next_temp > current_temp:
    #                 # count days
    #                 res.append(j - i)
    #                 no_greater_temp = False
    #                 break
    #         # reach the end, append 0
    #         if no_greater_temp == True:
    #             res.append(0)
    #         no_greater_temp = True
    #     return res

# test
solution = Solution()
temperatures = [73,74,75,71,69,72,76,73]
print(solution.dailyTemperatures(temperatures))


