from collections import defaultdict

class Solution:
    def uniqueLetterString(self, s: str) -> int:
        n = len(s)
        count = 0 # number of unique chars in substring
        hashmap = defaultdict(lambda: [-1]) # initialize map -1 (to calculate first window)
        
        # append all indeces to create the windows
        for i, char in enumerate(s):
            hashmap[char].append(i)

        # add length of string at the end (to calculate last window)
        for char in s:
            hashmap[char].append(n)
        
        # sum every window for each char
        # add the result to count
        for char in hashmap:
            # calculate length of windows and contribution
            for j in range(1, len(hashmap[char]) - 1):
                count += (hashmap[char][j] - hashmap[char][j - 1]) * (hashmap[char][j+1] - hashmap[char][j])

        return count
    
solution = Solution()
print(solution.uniqueLetterString("LEETCODE"))