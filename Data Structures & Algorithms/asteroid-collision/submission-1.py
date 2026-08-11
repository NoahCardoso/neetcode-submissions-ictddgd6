class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        i = 0

        while i < len(asteroids):
            if asteroids[i] < 0 and (stack == [] or stack[-1] < 0):
                stack.append(asteroids[i])
                i += 1
                continue
            if asteroids[i] >= 0 :
                stack.append(asteroids[i])
                i += 1
            else:
                r = stack.pop()
                larger = asteroids[i]
                if abs(r) > abs(asteroids[i]):
                    larger = r
                if r + asteroids[i] == 0:
                    i += 1
                elif larger >= 0:
                    stack.append(larger)
                    i += 1
                else:
                    asteroids[i] = larger
        return stack
                
