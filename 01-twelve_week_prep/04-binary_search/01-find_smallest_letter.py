from typing import List

class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        # binary search
        left = 0
        right = len(letters) - 1

        while left <= right:
            mid = (left + right) // 2 # get mid

            # no smallest, check upper half
            if letters[mid] <= target:
                left = mid + 1
            else:            
                right = mid - 1

        # no greatest letter found, return char at index 0
        if left >= len(letters):
            return letters[0]
        return letters[left]

# test
letters = ["c","f","j"]
target = "a"
solution = Solution()
print(solution.nextGreatestLetter(letters, target))
letters = ["c","f","j"]
target = "c"
print(solution.nextGreatestLetter(letters, target))
letters = ["x","x","y","y"]
target = "z"
print(solution.nextGreatestLetter(letters, target))
