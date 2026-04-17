class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        numbers = []
        
        for token in tokens:
            if token == "+":
                numbers.append(int(numbers.pop()) + int(numbers.pop()))
            elif token == "-":
                a = int(numbers.pop())
                numbers.append(int(numbers.pop()) - a)
            elif token == "*":
                numbers.append(int(numbers.pop()) * int(numbers.pop()))
            elif token == "/":
                a = int(numbers.pop())
                numbers.append(int(int(numbers.pop()) / a))
            else:
                numbers.append(int(token))
            print(numbers)
        if len(numbers) == 0:
            return None
        return numbers[-1]
