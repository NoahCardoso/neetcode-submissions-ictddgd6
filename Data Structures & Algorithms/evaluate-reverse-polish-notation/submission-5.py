class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:

            if token.isnumeric() or token[1::].isnumeric():
                stack.append(int(token))
            elif len(stack) > 1:
                b = stack.pop()
                a = stack.pop()
                if token == "+":
                    stack.append(a+b)
                elif token == "-":
                    stack.append(a-b)
                elif token == "*":
                    stack.append(a*b)
                elif token == "/":
                    stack.append(int(a/b))
        if stack:
            return stack[0]
        return -1


