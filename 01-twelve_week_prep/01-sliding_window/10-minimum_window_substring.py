from collections import defaultdict


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # two pointers
        if len(s) < len(t):  # edge case
            return ""

        # create dict t
        t_dict = defaultdict(int)

        for char in t:
            t_dict[char] += 1

        s_dict = defaultdict(int)
        start = 0

        # to compare both dictionaries
        have, need = 0, len(t_dict)
        result_indexes = [-1, -1]  # save start and end indexes for min window
        result_length = float("inf")

        # iterate string s
        for end, current_char in enumerate(s):
            # add current char to dictionary
            s_dict[current_char] += 1

            # check if the char have the same count
            if (current_char in t_dict
                    and s_dict[current_char] == t_dict[current_char]):
                # we have 1 more char
                have += 1

            while have == need:
                # update result
                if (end - start + 1) < result_length:  # compare lengths
                    result_indexes = [start, end]
                    result_length = end - start + 1
                # pop from the left
                s_dict[s[start]] -= 1
                # check the have
                if (s[start] in t_dict
                        and s_dict[s[start]] < t_dict[s[start]]):
                    have -= 1
                # decrease window size
                start += 1

        start, end = result_indexes

        # if there is no window
        if result_length == float("inf"):
            return ""

        return s[start: end + 1]


# Complexity
# Time: O(n)
# Space: O(n)

# TEST
solution = Solution()
s = "ADOBECODEBANC"
t = "ABC"
print(solution.minWindow(s, t))
s = "a"
t = "a"
print(solution.minWindow(s, t))
s = "a"
t = "aa"
print(solution.minWindow(s, t))
