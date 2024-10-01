from typing import List

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        answer, solution = [], []

        # takes an integer, n
        def backtrack(x):
            #base case
            if len(solution) == k:
                answer.append(solution[:])
                return
            
            # check if we have enough nums
            left = x
            still_need = k - len(solution)

            # we have more numbers left than we need
            if left > still_need: 
                # recursive call, we continue with the next number
                backtrack(x - 1)
            
            # use the number
            solution.append(x)
            backtrack(x - 1)
            # undo
            solution.pop()

        backtrack(n)
        return answer

sol = Solution()
n = 4
k = 2
print(sol.combine(n, k))
n = 1
k = 1
print(sol.combine(n, k))