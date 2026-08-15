class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        alive = True
        for ch in asteroids:
            alive = True

            while stack and alive and stack[-1]>0 and ch < 0:
                if abs(stack[-1]) < abs(ch):
                    stack.pop()
                elif abs(stack[-1]) == abs(ch):
                    stack.pop()
                    alive = False
                else:
                    alive = False
            if alive:
                stack.append(ch)
        return stack