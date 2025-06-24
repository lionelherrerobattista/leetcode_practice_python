class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        count = 0

        # window of size 3
        # compare chars a, b and c
        # start from index 2 and count chars backwards
        for i in range(2, len(s)):
            # save chars
            a = s[i]
            b = s[i - 1]
            c = s[i - 2]
            # comparison
            if (a != b and a != c and b != c):
                count += 1

        return count


solution = Solution()
s = "xyzzaz"
print(solution.countGoodSubstrings(s))
s = "aababcabc"
print(solution.countGoodSubstrings(s))
