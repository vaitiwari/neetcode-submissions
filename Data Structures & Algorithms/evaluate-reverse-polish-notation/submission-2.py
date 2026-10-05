class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        for i in tokens:
            if i == "+":
                val=int(stack[-1])+int(stack[-2])
                stack.pop()
                stack.pop()
                stack.append(val)
            elif i == "-":
                val=int(stack[-2])-int(stack[-1])
                stack.pop()
                stack.pop()
                stack.append(val)
            elif i == "*":
                val=int(stack[-2])*int(stack[-1])
                stack.pop()
                stack.pop()
                stack.append(val)
            elif i == "/":
                val=int(int(stack[-2])/int(stack[-1]))
                stack.pop()
                stack.pop()
                stack.append(val)
            else:
                stack.append(int(i))
        return stack[-1]