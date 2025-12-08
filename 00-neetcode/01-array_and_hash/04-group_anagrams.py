from collections import defaultdict
from typing import List

# https://leetcode.com/problems/group-anagrams/description/


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)  # save the freq of the words in strs

        for word in strs:
            count = [0] * 26  # a-z

            # create the frequency hashmap
            for letter in word:
                count[ord(letter) - ord("a")] += 1

            # append to array
            result[tuple(count)].append(word)  # touple, to make it immutable

        return list(result.values())

# Complexity
# Time: O(n * m) - loop each string and then each letter from the string
# Complexity: O(n * m) - a dictionary that has a list


sol = Solution()
result = sol.groupAnagrams(["act", "pots", "tops", "cat", "stop", "hat"])
print(result)
result = sol.groupAnagrams(["x"])
print(result)
