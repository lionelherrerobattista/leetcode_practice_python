from collections import defaultdict

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # edge case
        if len(s1) > len(s2):
            return False
        # create freq s1 and s2
        freq_s1 = defaultdict(int) # store frequency
        freq_s2 = defaultdict(int)
        for i in range(len(s1)):
            freq_s1[s1[i]] += 1
            freq_s2[s2[i]] += 1

        # check if equal
        if freq_s1 == freq_s2:
            return True # there is a permutation

        # init pointers
        left = 0
        # check for permutation
        for right in range(len(s1), len(s2)):
            # check frequency of chars in s2
            # remove left char
            char_to_remove = s2[left]
            freq_s2[char_to_remove] -= 1
            if freq_s2[char_to_remove] <= 0:
                del freq_s2[char_to_remove]
            # add right char
            char_to_add = s2[right]
            freq_s2[char_to_add] += 1
            # compare
            if freq_s1 == freq_s2:
                return True
            # increase left pointer
            left += 1
        # reached end, no permutation
        return False

# Complexity
# Time: O(n) check all chars in s2 string
# Space: O(26) dictionary with at most 26 English lowercase letters

# Tests
solution = Solution()
s1 = "ab"
s2 = "eidbaooo"
print(solution.checkInclusion(s1, s2))
s1 = "ab"
s2 = "eidboaoo"
print(solution.checkInclusion(s1, s2))

