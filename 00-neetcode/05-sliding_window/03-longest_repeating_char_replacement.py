class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # loop string, with two pointers
        left = 0
        max_length = 0
        char_counts = [0] * 26  # 26 english letters

        # keep moving right pointer (sliding window)
        for right, current_char in enumerate(s):
            # increase char count
            char_counts[ord(current_char) - 65] += 1  # 65, ASCII "A"
            current_length = right - left + 1
            # total number of char - count of max char,
            # gives us the amount of chars to change
            # should be less than k
            while current_length - max(char_counts) > k:
                # while it remains invalid, move left
                char_left = s[left]
                char_counts[ord(char_left) - 65] -= 1
                left += 1
                current_length = right - left + 1

            # check max length
            max_length = max(current_length, max_length)

        return max_length

# Complexity:
# Time: O(n * m) - Loop through each char, n total chars, m unique chars
# Space: O(26) - 26 uppercase english letters in array


sol = Solution()
s = "XYYX"
k = 2
print(sol.characterReplacement(s, k))

s = "AAABABB"
k = 1
print(sol.characterReplacement(s, k))

s = "ABAA"
k = 0
print(sol.characterReplacement(s, k))
