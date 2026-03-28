class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for a in asteroids:
            # While `a` is negative and last in stack is positive
            while stack and a < 0 and stack[-1] > 0:
                if stack[-1] < abs(a):
                    stack.pop()
                    continue
                elif stack[-1] == abs(a):
                    stack.pop()
                    break
                else:
                    break
            else:
                stack.append(a)
        return stack