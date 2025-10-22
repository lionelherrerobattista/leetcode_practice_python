from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # edge case, no digits
        if len(digits) == 0:
            return []

        digit_to_letter = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }
        res = []

        # iterate trough the array of digits
        def backtracking(i, current_string_array):  # choice one letter for each number
            if len(current_string_array) == len(digits):
                res.append("".join(current_string_array))  # create the string
                return

            # choice
            possible_letters = digit_to_letter[digits[i]]

            # check all combinatinons for that digit
            for letter in possible_letters:
                current_string_array.append(letter)
                # create new string, don't mutate
                backtracking(i + 1, current_string_array)
                # undo
                current_string_array.pop()
                # continue with next letter

        backtracking(0, [])

        return res

# Complexity
# Time: O(n * 4^n) - join strings, 4 letter combinations worst case
# Space: O(h) - call stack ?
