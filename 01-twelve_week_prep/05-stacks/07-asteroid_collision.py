from typing import List

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for asteroid in asteroids:
            # if the asteroid is negative, we check collision
            while stack and asteroid < 0 and stack[-1] > 0:
                # calculate outcome
                diff = asteroid + stack[-1] 
                if diff < 0:
                    # remove previous asteroid
                    stack.pop()
                elif diff > 0:
                    # asteroid is destroyed
                    asteroid = 0 # to avoid adding it to stack
                else:
                    # both are destroyed
                    asteroid = 0
                    stack.pop()
            if asteroid != 0: # add to stack
                stack.append(asteroid)
        return stack

# tests
solution = Solution()
asteroids = [5,10,-5]
print(solution.asteroidCollision(asteroids))
asteroids = [8,-8]
print(solution.asteroidCollision(asteroids))
asteroids = [10,2,-5]
print(solution.asteroidCollision(asteroids))
asteroids = [-2,-1,1,2]
print(solution.asteroidCollision(asteroids))




