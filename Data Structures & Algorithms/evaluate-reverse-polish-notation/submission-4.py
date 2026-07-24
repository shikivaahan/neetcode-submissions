class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        stack = []
        operators = {'+', '-', '*', '/'}

        for num in tokens:
            if num in operators:
                num2 = stack.pop()
                num1 = stack.pop()
                result = self.evaluate(num1, num2, num)
                stack.append(result)
            else:
                stack.append(int(num))
        return stack[0]

    def evaluate(self, num1: str , num2: str, operator: str) -> str:
        num1 = int(num1)
        num2 = int(num2)
        match operator:
            case '+':
                return num1 + num2
            case '-':
                return num1 - num2
            case '*':
                return num1 * num2
            case '/':
                return int(num1 / num2)
        