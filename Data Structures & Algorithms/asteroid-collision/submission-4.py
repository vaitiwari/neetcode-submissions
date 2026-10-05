class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for i in asteroids:
            while stack and i < 0 and stack[-1] > 0:
                if stack[-1] == -i:    # equal → both die
                    stack.pop()
                    break
                elif stack[-1] < -i:   # top is smaller → top dies, keep going
                    stack.pop()
                else:                  # top is bigger → i dies
                    break
            else:
                stack.append(i)
        return stack