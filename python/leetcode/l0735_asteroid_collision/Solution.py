from typing import List

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        """
        We can keep appending to the stack until there is atleast two values and we can keep 
        operating on the stack until we can't anymore and slowly keep adding values to the stack until there is no more 
        asteroids left to add, at which point we can add the stack. We can still apply the same logic and do the comparisons on the 
        popped value vs the new top and see what should be removed.

        diregard everything i said before, so many edge cases kept failing.
        if the current one is negative, and the head of the stack is positive, it's clear we might have some work to do. We should keep going until either:
            1. the current asteroid is destroyed
            2. the current asteroid lives and is popped into the stack
            3. they are both destroyed

        Which means, we keep going until the current asteroid is destroyed or there is nothing left to compare this current_asteroid to.
        """

        stack = []

        for i in range(len(asteroids)):
            if len(stack) < 1 or asteroids[i] > 0:
                stack.append(asteroids[i])
                continue

            if stack[-1] < 0:
                stack.append(asteroids[i])
                continue

            destroyed = False
            while len(stack) >= 1 and stack[-1] > 0 and not destroyed:
                current_asteroid = asteroids[i]
                previous_asteroid = stack[-1]

                if abs(current_asteroid) > abs(previous_asteroid):
                    stack.pop()
                elif abs(current_asteroid) == abs(previous_asteroid):
                    stack.pop()
                    destroyed = True
                else:
                    destroyed = True

            if not destroyed:
                stack.append(asteroids[i])

        return stack

# print(Solution().asteroidCollision([5,10,-5]))
# print(Solution().asteroidCollision([8, -8]))
# print(Solution().asteroidCollision([-2,-1,1,2]))
# print(Solution().asteroidCollision([-2,-8,1,-2]))
print(Solution().asteroidCollision([10,2,-5]))
