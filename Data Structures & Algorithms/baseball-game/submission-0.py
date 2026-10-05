class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack1=[]
        new_list=[]
        for op in operations:
            if op=="+":
                var=stack1[-1]+stack1[-2]
                stack1.append(var)
            elif op=="D":
                var=2*stack1[-1]
                stack1.append(var)
            elif op=="C":
                stack1.pop(-1)
            else:
                stack1.append(int(op))
        print(stack1)
        return sum(stack1)
