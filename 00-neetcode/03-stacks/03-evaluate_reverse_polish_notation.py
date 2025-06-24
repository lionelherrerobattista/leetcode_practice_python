from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operands_stack = []  # save tokens

        # store token in the stack until we get to an operand
        for token in tokens:
            # calculate operations
            if token == "+":
                operands_stack.append(
                    operands_stack.pop() + operands_stack.pop())
            elif token == "-":
                second_operand = operands_stack.pop()
                first_operand = operands_stack.pop()
                operands_stack.append(first_operand - second_operand)
            elif token == "*":
                operands_stack.append(
                    operands_stack.pop() * operands_stack.pop())
            elif token == "/":
                second_operand = operands_stack.pop()
                first_operand = operands_stack.pop()
                operands_stack.append(int(first_operand / second_operand))
            else:
                operands_stack.append(int(token))

        return operands_stack.pop()


tokens = ["2", "1", "+", "3", "*"]
tokens = ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
sol = Solution()
result = sol.evalRPN(tokens)
print(result)
