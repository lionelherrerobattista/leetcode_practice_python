from typing import List


class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ""
        # add delimiter with the word lenght e.g.: 4#test
        for word in strs:
            encoded_string += str(len(word)) + "#" + word

        return encoded_string

    def decode(self, s: str) -> List[str]:
        decoded_string = []
        i = 0

        # decode the string
        while i < len(s):
            j = i
            # check integers until delimiter
            while s[j] != "#":
                j += 1
            # save length, start and end
            word_length = int(s[i:j])
            word_start = j + 1  # word start
            word_end = j + 1 + word_length  # word end
            # extract word and append
            decoded_string.append(s[word_start:word_end])
            # continue from last char after word
            i = word_end

        return decoded_string
