class MinStack:

    def __init__(self):
        self.stack = [] 
        self.min_element_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)

        if self.min_element_stack == []:
            self.min_element_stack.append(val)
        else: 
            self.min_element_stack.append(min(val, self.min_element_stack[-1]))

    def pop(self) -> None:
        self.stack.pop() 
        self.min_element_stack.pop()
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.min_element_stack[-1]
        
        
