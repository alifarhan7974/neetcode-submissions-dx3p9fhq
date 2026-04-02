class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        evaluate = { 
            "+" : lambda x, y: x + y,
            "-" : lambda x, y: x - y,
            "*" : lambda x, y: x * y,
            "/" : lambda x, y: int(x / y) # Truncates neg nums correctly
        }

        for item in tokens: 
            if item in evaluate: 
                second = stack.pop()
                first = stack.pop() 
                stack.append(evaluate[item](first, second))   
            else: 
                stack.append(int(item))

        return stack.pop()

                
        