from collections import defaultdict


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # edge case, no chars
        if len(s) == 0:
            return 0

        # two pointers
        # one, at the start
        # second, will check next char
        left = 0

        # length is right_pointer - left_pointer + 1
        # keep track of max length, and return at the end
        max_length = 0

        # keep track of repeating chars:
        # set, only has unique values
        # instant access
        char_set = set()

        # check next chars in s
        for right, current_char in enumerate(s):
            # check the current char in the dict
            while current_char in char_set:
                # remove the chars until repeated (included)
                char_set.remove(s[left])
                left += 1

            # no repeted chars
            # add the next char to dict
            char_set.add(current_char)

            # update the max length
            current_length = right - left + 1
            max_length = max(current_length, max_length)

        return max_length

# Complexity
# Time: O(n) - iterate once
# Space: O(m) - use of set, m total unique chars


sol = Solution()
s = "zxyzxyz"
print(sol.lengthOfLongestSubstring(s))

s = "xxxx"
print(sol.lengthOfLongestSubstring(s))

s = "pwwkew"
print(sol.lengthOfLongestSubstring(s))
