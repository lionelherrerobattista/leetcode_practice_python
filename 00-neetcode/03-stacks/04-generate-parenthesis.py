from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # add open parenthesis if open < n
        # add closing parenthesis if closed < open

        stack = []
        res = []

        def backtrack(openN, closedN):
            # base case
            if openN == closedN == n:
                res.append("".join(stack))  # add to res stack

            # add "("
            if openN < n:
                stack.append("(")
                backtrack(openN + 1, closedN)  # update number
                stack.pop()  # to reset global

            if closedN < openN:
                stack.append(")")
                backtrack(openN, closedN + 1)
                stack.pop()

        # run backtraking function
        backtrack(0, 0)
        return res
