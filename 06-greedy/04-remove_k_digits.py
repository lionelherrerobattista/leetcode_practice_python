class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = [] # monotonic increasing
        # check the chars
        for digit in num:
            # check still within k
            # if the previous element in stack is greater, 
            # we should pop it
            while k > 0 and stack and stack[-1] > digit:
                k -= 1 # update k
                stack.pop()
            # append the element 
            stack.append(digit)
        
        # if we still have k element to pop
        while k > 0 and stack:
            k -= 1 # update k
            stack.pop()

        # remove leading 0
        result = "".join(stack).lstrip('0')

        # if string is empty
        if result == "":
            return '0'
        
        return result

# tests
solution = Solution()
num = "1432219"
k = 3
print(solution.removeKdigits(num, k))
num = "10200"
k = 1
print(solution.removeKdigits(num, k))
num = "10"
k = 2
print(solution.removeKdigits(num, k))