class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) == 1:  # edge case, only 1 char
            return False

        # create stack - LIFO
        char_stack = []
        close_to_open = {
            ")": "(",
            "}": "{",
            "]": "["
        }

        # loop string
        for char in s:
            if char in close_to_open:  # closing brackets - pop and compare
                if len(char_stack) == 0:
                    # no opening bracket
                    return False

                previous_char = char_stack.pop()
                if previous_char != close_to_open[char]:
                    # no matching pair - return false
                    return False
                # if match continue
            # opening brackets - push
            else:
                char_stack.append(char)

        if len(char_stack) > 0:  # open brackets remaining
            return False

        # end loop, valid string
        return True

# Complexity
# Time: O(n) - visit every char of the string
# Space: O(n) - stack to keep track of open brackets
