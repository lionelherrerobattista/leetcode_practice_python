from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        result = []
        digitToChar = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }
        # define backtrack function
        def backtrack(i, currString): # index, string we are working with
            # base case
            if len(currString) == len(digits): # we mapped every char
                result.append(currString) # append the resulting str
                return
            # take current digit and map it to char
            for char in digitToChar[digits[i]]:
                # move to next index
                # add char to the currentstring
                backtrack(i + 1, currString + char) 
        # call function
        if digits: # to avoid returning [""]
            backtrack(0, "")

        return result

solution = Solution()
print(solution.letterCombinations("2"))
print(solution.letterCombinations("23"))

