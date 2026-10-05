class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack=[]

        for i in asteroids:
            alive=True
            if i >0:
                stack.append(i)
            while alive and i < 0 and stack and stack[-1]>0:
                if abs(stack[-1])==abs(i):
                    stack.pop()
                    alive=False
                elif stack[-1]>abs(i): 
                     alive=False
                else:
                    stack.pop()
                    # stack.append(i)
            if alive and i < 0:   # ← add this
                stack.append(i)
        return stack

