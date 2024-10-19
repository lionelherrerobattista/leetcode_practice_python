from collections import deque


class Solution:
    def integerReplacement(self, n: int) -> int:
        # solution bfs
        queue = deque([n])
        seen = set() # memoization
        seen.add(n)
        answer = 0

        while queue:
            for _ in range(len(queue)):
                current = queue.popleft()
                # base case
                if current == 1:
                    return answer
                
                if current % 2 != 0: # odd case
                    #sanity check 
                    if current + 1 not in seen:
                        queue.append(current + 1)
                        seen.add(current + 1)
                    if current - 1 not in seen:
                        queue.append(current - 1)
                        seen.add(current - 1)
                else: # even case
                    if current // 2 not in seen:
                        queue.append(current // 2)
                        seen.add(current // 2)
            answer += 1
        return answer
    
    # brute force, fails test case
    # def integerReplacement(self, n: int) -> int:
        # num_operations_plus = 0
        # num_operations_minus = 0
        # aux_n = n
        # # convert to 1
        # while aux_n != 1:
        #     # check if even
        #     if aux_n % 2 == 0:
        #         aux_n = aux_n / 2
        #     else: # if odd
        #         # other condition?
        #         aux_n = aux_n + 1
        #     num_operations_plus += 1
        # aux_n = n
        # while aux_n != 1:
        #     # check if even
        #     if aux_n % 2 == 0:
        #         aux_n = aux_n / 2
        #     else: # if odd
        #         # other condition?
        #         aux_n = aux_n - 1
        #     num_operations_minus += 1

        # return num_operations_plus if num_operations_plus < num_operations_minus else num_operations_minus

# test
solution = Solution()
n = 10000
print(solution.integerReplacement(n))