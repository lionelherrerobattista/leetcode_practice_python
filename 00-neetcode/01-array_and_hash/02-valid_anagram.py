from collections import defaultdict


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # edge case
        if len(s) != len(t):
            return False

        # create hash maps
        s_hashmap = defaultdict(int)
        t_hashmap = defaultdict(int)

        # add chars to hashmap
        for i in range(0, len(s)):
            s_hashmap[s[i]] += 1
            t_hashmap[t[i]] += 1

        # compare hashmaps
        if s_hashmap != t_hashmap:
            return False

        return True

# Complexity:
# Time: O(n + m) - iterate through each element once in both strings
# Space: O(1) - although we create hashmaps, always 26 chars long


# # Unicode
# class Solution:
#     def isAnagram(self, s: str, t: str) -> bool:
#         # edge case
#         if len(s) != len(t):
#             return False

#         # create arrays, 26 lowercase English letters
#         s_hashmap = [0] * 26
#         t_hashmap = [0] * 26

#         # add chars to hashmap
#         for i in range(0, len(s)):
# 		        # index = number representation of char
#             s_hashmap[ord(s[i]) - ord('a')] += 1 # store in index
#             t_hashmap[ord(t[i]) - ord('a')] += 1

#         # compare hashmaps
#         if s_hashmap != t_hashmap:
#             return False

#         return True

# # Complexity:
# # Time: O(n + m) - iterate through each element once in both strings
# # Space: O(1) - although we create arrays, always 26 chars long
