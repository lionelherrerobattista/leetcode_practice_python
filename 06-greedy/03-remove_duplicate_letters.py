class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        # find duplicates (dict?)
        lookup = {}
        # keep track of the greatest index of each char
        for i, letter in enumerate(s):
            lookup[letter] = i
        stack = [] # monotonic increasing
        seen = set() # check if we've seen the char

        for i, current_letter in enumerate(s):
            # check if we've seen the char
            if current_letter in seen:
                continue
            # new char, check if we should pop the last char in stack
            # and add the current char
            # keep monotonic increasing stack
            while stack and stack[-1] > current_letter and lookup[stack[-1]] > i:
                seen.remove(stack[-1]) # as it will be used later
                stack.pop()
            # append new char
            stack.append(current_letter)
            seen.add(current_letter)

        return "".join(stack)

# test
solution = Solution()
s = "bcabc"
print(solution.removeDuplicateLetters(s))
s = "cbacdcbc"
print(solution.removeDuplicateLetters(s))