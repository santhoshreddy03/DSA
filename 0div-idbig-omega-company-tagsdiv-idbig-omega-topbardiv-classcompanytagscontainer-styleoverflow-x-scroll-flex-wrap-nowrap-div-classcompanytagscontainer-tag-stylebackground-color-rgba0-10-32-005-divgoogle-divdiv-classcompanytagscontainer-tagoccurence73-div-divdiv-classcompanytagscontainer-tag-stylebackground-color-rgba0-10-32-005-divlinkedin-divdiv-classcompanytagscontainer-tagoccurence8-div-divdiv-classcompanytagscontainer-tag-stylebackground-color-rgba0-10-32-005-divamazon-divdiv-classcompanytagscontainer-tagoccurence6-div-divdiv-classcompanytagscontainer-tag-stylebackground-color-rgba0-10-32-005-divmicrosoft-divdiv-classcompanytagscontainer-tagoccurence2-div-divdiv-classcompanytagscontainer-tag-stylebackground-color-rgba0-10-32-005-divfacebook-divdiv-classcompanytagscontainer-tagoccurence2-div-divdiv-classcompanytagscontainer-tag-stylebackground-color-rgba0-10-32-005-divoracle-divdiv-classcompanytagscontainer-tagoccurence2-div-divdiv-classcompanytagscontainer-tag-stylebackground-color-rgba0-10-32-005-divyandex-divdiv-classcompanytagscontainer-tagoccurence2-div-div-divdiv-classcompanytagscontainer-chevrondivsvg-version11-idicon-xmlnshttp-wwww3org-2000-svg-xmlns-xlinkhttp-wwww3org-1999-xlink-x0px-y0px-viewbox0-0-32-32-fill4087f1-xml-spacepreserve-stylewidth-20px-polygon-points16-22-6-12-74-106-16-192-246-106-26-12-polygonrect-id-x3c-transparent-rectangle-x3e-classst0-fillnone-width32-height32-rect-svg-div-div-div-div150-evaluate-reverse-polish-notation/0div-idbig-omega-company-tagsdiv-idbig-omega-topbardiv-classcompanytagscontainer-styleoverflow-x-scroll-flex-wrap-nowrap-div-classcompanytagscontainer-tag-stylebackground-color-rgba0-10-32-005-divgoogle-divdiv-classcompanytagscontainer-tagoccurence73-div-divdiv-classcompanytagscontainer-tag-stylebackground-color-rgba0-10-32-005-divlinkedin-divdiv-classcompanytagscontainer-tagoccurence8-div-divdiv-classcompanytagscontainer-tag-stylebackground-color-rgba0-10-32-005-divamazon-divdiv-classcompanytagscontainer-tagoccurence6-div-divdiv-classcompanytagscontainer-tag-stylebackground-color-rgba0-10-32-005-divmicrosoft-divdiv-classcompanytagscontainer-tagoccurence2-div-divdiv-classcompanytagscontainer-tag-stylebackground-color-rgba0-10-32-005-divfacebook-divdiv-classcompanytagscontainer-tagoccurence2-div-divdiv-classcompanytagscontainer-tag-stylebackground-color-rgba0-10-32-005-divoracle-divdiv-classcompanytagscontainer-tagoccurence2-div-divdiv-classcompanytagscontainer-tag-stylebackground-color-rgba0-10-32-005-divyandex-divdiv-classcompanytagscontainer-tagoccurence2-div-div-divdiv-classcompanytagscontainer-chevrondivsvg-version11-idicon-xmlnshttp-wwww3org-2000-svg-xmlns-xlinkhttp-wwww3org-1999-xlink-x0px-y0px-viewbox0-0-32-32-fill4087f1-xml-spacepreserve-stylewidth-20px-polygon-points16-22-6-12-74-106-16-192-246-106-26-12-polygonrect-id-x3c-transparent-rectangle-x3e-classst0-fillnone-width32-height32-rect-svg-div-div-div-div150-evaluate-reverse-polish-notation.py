class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        for i in tokens:
            if i=="+":
                x=stack.pop() + stack.pop()
                stack.append(x)
            elif i=="-":
                a,b=stack.pop(),stack.pop()
                x=b-a
                stack.append(x)
            elif i=="*":
                x=stack.pop() * stack.pop()
                stack.append(x)
            elif i=="/":
                a,b=stack.pop(),stack.pop()
                x=int(float(b)/a)
                stack.append(int(x))
            else:
                stack.append(int(i))
        return stack[0]
        