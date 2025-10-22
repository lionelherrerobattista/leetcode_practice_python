from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        palindromes = []
        result = []

        def is_palindrome(left_pointer, right_pointer):
            while left_pointer < right_pointer:
                if s[left_pointer] != s[right_pointer]:
                    # not a palindrome
                    return False

                left_pointer += 1
                right_pointer -= 1

            return True  # is a palindrome

        def backtracking(start):
            # base cases
            # reach end of string
            if start == len(s):
                result.append(palindromes.copy())
                return

            # iterate all susbtrings from i to the end
            for end in range(start, len(s)):
                # check if substring is palindrome
                if is_palindrome(start, end):
                    palindromes.append(s[start: end + 1])  # last not included
                    # backtrack
                    backtracking(end + 1)
                    # undo
                    palindromes.pop()

        backtracking(0)

        return result
