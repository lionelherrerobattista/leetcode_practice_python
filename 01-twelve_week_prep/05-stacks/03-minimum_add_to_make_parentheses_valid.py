class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        l_count = r_count = added = 0

        # go left to right in string
        for char in s:
            # check the parenthesis type
            if char == '(':
                l_count += 1
            else:
                if r_count < l_count:
                    # we are sure that there is a left parenthesis
                    # to close it:
                    r_count += 1
                else:
                    # left parenthesis is invalid
                    # we need to add a right parenthesis:
                    added += 1
        # we need to account for the left parenthesis
        # that were closed:
        added += l_count - r_count
        return added
    
# time: O(n) space: O(1)

# test
solution = Solution()
s = "())"
print(solution.minAddToMakeValid(s))
s = "((("
print(solution.minAddToMakeValid(s))