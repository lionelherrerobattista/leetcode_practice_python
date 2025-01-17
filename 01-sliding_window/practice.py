from collections import defaultdict


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # check edge case, s2 length shorter than s1
        if len(s1) > len(s2):
            return False

        # create dictionary for s1 and s2, k length
        s1_dict = defaultdict(int)
        s2_dict = defaultdict(int)

        for i in range(len(s1)):
            s1_dict[s1[i]] += 1
            s2_dict[s2[i]] += 1

        # compare dictionaries
        if s1_dict == s2_dict:
            return True

        # create window with fixed length
        start = 0
        end = len(s1)

        while end < len(s2):
            # add and remove chars
            # remove start char and increase index
            s2_dict[s2[start]] -= 1

            if s2_dict[s2[start]] <= 0:
                del s2_dict[s2[start]]

            start += 1

            # add end char and increase index
            s2_dict[s2[end]] += 1
            end += 1

            # compare
            if s1_dict == s2_dict:
                return True

        # reached end, no permutation
        return False


solution = Solution()
s1 = "ab"
s2 = "eidbaooo"
print(solution.checkInclusion(s1, s2))
s1 = "ab"
s2 = "eidboaoo"
print(solution.checkInclusion(s1, s2))
