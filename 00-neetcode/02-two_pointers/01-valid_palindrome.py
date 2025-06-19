class Solution:
    def isPalindrome(self, s: str) -> bool:
        # two pointers, left and right
        left = 0
        right = len(s) - 1

        def isAlphanumeric(character):
            return ((ord("a") <= ord(character) <= ord("z"))  # check letter
                    or (ord("A") <= ord(character) <= ord("Z"))  # check letter
                    or (ord("0") <= ord(character) <= ord("9")))  # check num

        # check if equal
        while left < right:
            # ignore alphanumeric chars
            while (not isAlphanumeric(s[left])) and left < right:
                left += 1

            while (not isAlphanumeric(s[right])) and right > left:
                right -= 1

            char_left = str.lower(s[left])
            char_right = str.lower(s[right])

            # compare
            # case insensitive (to lower, then compare)
            if (char_left != char_right):
                return False  # not palindrome

            left += 1
            right -= 1

        return True  # palindrome

# Complexity
# Time: O(n) - go through the string once
# Space: O(1) - no use of extra data structure


solution = Solution()
s = "Was it a car or a cat I saw?"
result = solution.isPalindrome(s)
print(result)
s = ".,"
result = solution.isPalindrome(s)
print(result)
s = "0P"
result = solution.isPalindrome(s)
print(result)
