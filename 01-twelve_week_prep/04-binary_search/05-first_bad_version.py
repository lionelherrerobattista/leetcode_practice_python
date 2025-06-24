# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:


class Solution:
    def firstBadVersion(self, n: int) -> int:
        left, right = 1, n
        while left < right: # we leave when left == right
            mid = (left + right) // 2

            if isBadVersion(mid): # provided by leetcode
                right = mid # we want to keep the last False
            else:
                left = mid + 1
        return left # or right
                

# my solution:
# class Solution:
#     def firstBadVersion(self, n: int) -> int:
#         left, right = 1, n
#         while left <= right:
#             mid = (left + right) // 2

#             # check current element
#             current_element = isBadVersion(mid)
#             # first version is the bad one
#             if current_element == True and mid == 1:
#                 return mid
#             # check previous version
#             previous_element = isBadVersion(mid - 1)
#             if previous_element == False and current_element == True:
#                 # found first bad version
#                 return mid
#             elif current_element == False:
#                 # all to the left are also False
#                 left = mid + 1
#             else:
#                 # current is True, left is also True: we can discard right
#                 right = mid - 1