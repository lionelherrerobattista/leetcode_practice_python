class Solution:
    def longestPalindrome(self, s: str) -> int:
        char_dict = {}
        res = 0
        # create hashmap for s
        # to get the counts of char
        # and count even values
        for char in s:
            if char in char_dict:
                char_dict[char] += 1
            else:
                char_dict[char] = 1

            # check if even
            if char_dict[char] % 2 == 0:
                res += 2 # matching pair

        # check if there is any odd value
        # we increase the count by 1
        # remaining char that can be in the middle
        for count in char_dict.values():
            if count % 2 != 0:
                res += 1
                break

        return res

# test
solution = Solution()
s = "abccccdd"
print(solution.longestPalindrome(s))
s = "a"
print(solution.longestPalindrome(s))