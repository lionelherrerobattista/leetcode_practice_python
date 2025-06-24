class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def nextValidChar(str, index):
            backspace = 0  # count '#' chars
            while index >= 0:
                # check if valid index
                if backspace == 0 and str[index] != "#":
                    break

                # if not, count backspaces
                if str[index] == "#":
                    backspace += 1
                else:
                    backspace -= 1

                # move index
                index -= 1
            return index  # next valid char

        # start from end
        pointer_s = len(s) - 1
        pointer_t = len(t) - 1

        # loop and compare both pointers
        # keep them inbounds
        # 'or' out of bounds handled in the loop
        while pointer_s >= 0 or pointer_t >= 0:
            # search valid index
            pointer_s = nextValidChar(s, pointer_s)
            pointer_t = nextValidChar(t, pointer_t)

            # get char or empty string if out of bounds
            char_s = s[pointer_s] if pointer_s >= 0 else ""
            char_t = t[pointer_t] if pointer_t >= 0 else ""

            # compare chars
            if char_s != char_t:
                return False

            # decrement pointers
            pointer_s -= 1
            pointer_t -= 1
        return True  # chars are all equal


solution = Solution()
s = "ab#c"
t = "ad#c"
print(solution.backspaceCompare(s, t))
s = "ab##"
t = "c#d#"
print(solution.backspaceCompare(s, t))
s = "a#c"
t = "b"
print(solution.backspaceCompare(s, t))
s = "xywrrmp"
t = "xywrrmu#p"
print(solution.backspaceCompare(s, t))
