from collections import defaultdict


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # edge case s1 is longer than s2
        if len(s1) > len(s2):
            return False  # no permutation possible

        # create 2 dict to store the letters in each string
        s1_dict = defaultdict(int)
        s2_dict = defaultdict(int)

        for index, char in enumerate(s1):
            s1_dict[s1[index]] += 1
            s2_dict[s2[index]] += 1

        # check if equal
        if s1_dict == s2_dict:
            return True

        # 2 pointers to iterate through the chars
        left = 0
        right = len(s1)

        # we check if the dicts are equal we return true
        while right < len(s2):
            # remove from left
            char_to_remove = s2[left]
            s2_dict[char_to_remove] -= 1

            if s2_dict[char_to_remove] == 0:
                del s2_dict[char_to_remove]

            # increase left by 1
            left += 1

            # add right + 1 char
            char_to_add = s2[right]
            s2_dict[char_to_add] += 1

            # compare and return if equal
            if s1_dict == s2_dict:
                return True

            right += 1

        # else no permutation, return false
        return False

# Complexity
# Time: O(n) - only iterate through each element once
# Complexity: O(1) - Worst case, store 26 English letters


sol = Solution()
s1 = "abc"
s2 = "lecabee"
print(sol.checkInclusion(s1, s2))

s1 = "abc"
s2 = "lecaabee"
print(sol.checkInclusion(s1, s2))
