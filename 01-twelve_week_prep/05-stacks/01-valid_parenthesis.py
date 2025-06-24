class Solution:
    def isValid(self, s: str) -> bool:
        hashmap = {
            ')':'(',
            '}':'{',
            ']':'['
        } # to check for eq. opening parenthesis
        stk = [] # stack to store opening parenthesis

        # check chars in string
        for c in s:
            if c not in hashmap: # if it is open parenthesis (not a key in)
                stk.append(c) # store in stack
            else: # a closing parenthesis
                if not stk: # we don't have opening equivalent
                    return False
                else:
                    popped = stk.pop()
                    # check last stored parenthesis
                    if popped != hashmap[c]:
                        return False

        # check if stack is empty
        if len(stk) != 0:
            return False # parentheses not closed
              
        return True # is valid
         
# test
solution = Solution()
s = "()"
print(solution.isValid(s))
s = "()[]{}"
print(solution.isValid(s))
s = "(]"
print(solution.isValid(s))
s = "([])"
print(solution.isValid(s))
s= "([)]"
print(solution.isValid(s))