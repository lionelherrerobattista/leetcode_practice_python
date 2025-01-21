from collections import defaultdict


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        longest = 0
        start = 0
        dict_s = defaultdict(int)

        # sliding window
        for end, _ in enumerate(s):
            # extend window until replacable chars > k
            dict_s[s[end]] += 1

            # check invalid string
            # more char to replace than k
            while (end - start + 1) - max(dict_s.values()) > k:
                # move start to make it valid again
                dict_s[s[start]] -= 1
                start += 1

            # update longest replacement
            longest = max(longest, (end - start + 1))

        return longest


# TESTS
solution = Solution()
s = "ABAB"
k = 2
print(solution.characterReplacement(s, k))
s = "AABABBA"
k = 1
print(solution.characterReplacement(s, k))
