from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        sol = []

        def backtrack(openn, close):
            # base case
            if len(sol) == n * 2: # pair of ()
                # append the result
                res.append(''.join(sol))
                return
            
            # check if we can add an open bracket
            if openn < n:
                sol.append('(')
                # we have one more open in the string
                backtrack(openn + 1, close)
                # undo
                sol.pop()

            # check if we can add a close bracket
            if openn > close:
                sol.append(')')
                # add one to close
                backtrack(openn, close + 1)
                # undo
                sol.pop()

        # call to function
        backtrack(0, 0)
        return res



# test:
solution = Solution()
n = 3
print(solution.generateParenthesis(n))
n = 1
print(solution.generateParenthesis(n))
            