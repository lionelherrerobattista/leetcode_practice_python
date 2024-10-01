from typing import List
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        # define the recursive function
        def dfs(i, cur, total):
            #base cases
            if total == target:
                # we append the current combination
                # a copy because we continue to modify it
                res.append(cur.copy())
                return
            # base if we go over the candidates 
            # or total is greater than target
            if i >= len(candidates) or total > target:
                return
            # two branch decision:
            # 1- append the current candidate
            cur.append(candidates[i])
            # call the recursive function and sum the current candidate
            dfs(i, cur, total + candidates[i])
            # 2- if we are not going to include the candidate
            cur.pop()
            dfs(i + 1, cur, total) # we move to the next candidate
        
        #start recursive function
        dfs(0, [], 0)
        return res

# test
candidates = [2,3,6,7]
target = 7
solution = Solution()
print(solution.combinationSum(candidates, target))

# recrusion
# def countdown(num):
#     if num == 0:
#         print("all done!")
#         return
#     print(num)
#     countdown(num - 1)

# countdown(10)

# def sumRange(num):
#     # base case
#     if num == 1:
#         return 1
#     return num + sumRange(num - 1)

# print(sumRange(5))

# def factorial(num):
#     #base case
#     if num == 1:
#         return 1
#     return num * factorial(num - 1)

# print(factorial(4))
