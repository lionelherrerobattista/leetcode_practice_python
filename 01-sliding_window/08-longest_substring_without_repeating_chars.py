from collections import defaultdict


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_length = 0
        s_dict = defaultdict(int)  # to save chars
        # two pointer, start at the beginning
        start = 0

        for end, _ in enumerate(s):
            # move right pointer, until repreating char
            s_dict[s[end]] += 1
            # if char is repeated,
            # move left pointer until first occurrence
            while s_dict[s[end]] > 1 and start < end:
                s_dict[s[start]] -= 1
                start += 1

            # calculate max length and compare with stored max
            max_length = max(max_length, end - start + 1)

        return max_length

# Complexity
# Time: O(n)
# Space: O(n)


# TEST
solution = Solution()
s = "abcabcbb"
print(solution.lengthOfLongestSubstring(s))
s = "bbbbb"
print(solution.lengthOfLongestSubstring(s))
s = "pwwkew"
print(solution.lengthOfLongestSubstring(s))
