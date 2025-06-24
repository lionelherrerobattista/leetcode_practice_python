from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        numLength = len(nums)
        answer, permutation = [], []

        def backtrack():
            # base case - reached max length
            if len(solution) == numLength:
                answer.append(permutation[:]) # upload a copy
                return
            
            for num in nums:
                if num not in permutation:
                    # we append the current number
                    permutation.append()
                    # call to recursive function
                    backtrack()
                    # we pop last num to travel the branch up
                    permutation.pop()
            
        backtrack()
        return answer
    # Time: O(n!), Space: O(n)
            

    # def permute(self, nums: List[int]) -> List[List[int]]:
    #       my solution
    #     res = []

    #     def permutationRecurse(permutationArray, currentElement, options):
    #         # append current element
    #         permutationArray.append(currentElement)
    #         # remove current element from options
    #         options.pop(options.index(currentElement))

    #         # base case - reached max length
    #         if len(permutationArray) == len(nums):
    #             res.append(permutationArray)
    #             return
    #         # execute recursive function
    #         for option in options:
    #             permutationRecurse(permutationArray.copy(), option, options.copy())
    #     #explore all options in root
    #     for num in nums:
    #         permutationRecurse([], num, nums.copy())

    #     print(res)
    #     return res
                
solution = Solution()
solution.permute([1,2,3])
solution.permute([0,1])
solution.permute([1])
            
            