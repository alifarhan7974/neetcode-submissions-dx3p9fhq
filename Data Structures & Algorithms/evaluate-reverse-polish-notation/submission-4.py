class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operands = {"+", "-", "*", "/"} # For O(1) lookup
        evaluate = { 
            "+" : lambda x, y: x + y,
            "-" : lambda x, y: x - y,
            "*" : lambda x, y: x * y,
            "/" : lambda x, y: int(x / y)
        }


        for item in tokens: 
            if item in operands: 
                second = stack.pop()
                first = stack.pop() 
                stack.append(evaluate[item](first, second))   
            else: 
                stack.append(int(item))

        return stack[0]

                
        