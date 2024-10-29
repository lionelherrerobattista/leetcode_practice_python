from typing import List
from collections import defaultdict

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        # edge case
        start_indexes = []
        if len(p) > len(s):
            return start_indexes
        left = 0
        right = len(p) - 1
        # store char frequency char:freq
        freq_s = defaultdict(int)
        freq_p = defaultdict(int)
        # check frequency in s
        for i in range(len(p)):
            freq_s[s[i]] += 1
        # check frequency in p until s length:
        for char in p:
            freq_p[char] += 1

        # compare dictionaries
        if freq_p == freq_s:
            start_indexes.append(left)

        # two pointer for s
        # check chars in s
        while right < len(s) - 1:
            # remove last char (left pointer)
            char_to_remove = s[left]
            freq_s[char_to_remove] -= 1
            # check if key == 0
            if freq_s[char_to_remove] == 0:
                del freq_s[char_to_remove] # remove the key

            # update left and right pointers
            left += 1
            right += 1
            
            # add another char (right pointer)
            new_char = s[right]
            freq_s[new_char] += 1

            # compare dictionaries
            if freq_p == freq_s:
                start_indexes.append(left)
        # return array
        return start_indexes

# Complexity
# Time: O(n) we check every single char in s 
# Space: O(n) we create hashmaps to count the ocurrences of chars

# tests
solution = Solution()
s = "cbaebabacd"
p = "abc"
print(solution.findAnagrams(s, p))
s = "baa"
p = "aa"
print(solution.findAnagrams(s, p))