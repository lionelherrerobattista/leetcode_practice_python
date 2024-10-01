def isPalindrome(x):
    """
    :type x: int
    :rtype: bool
    """
    # convert to string (char array)
    number_as_string = str(x)
    # compare string starting from last index
    index_end = len(number_as_string) - 1
    index_start = 0

    while index_end >= 0: # until last element
        if number_as_string[index_end] != number_as_string[index_start]:
            return False # if not equal return False
        # move to next element:
        index_end -= 1
        index_start += 1
    return True # if loop completes, all nums are equal. Return True
    