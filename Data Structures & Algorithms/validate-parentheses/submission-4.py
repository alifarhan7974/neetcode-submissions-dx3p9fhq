class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = []
        parentheses = {
            "{" : "}", 
            "(" : ")",
            "[" : "]"
        }
        
        for p in s: 
            # Open Bracket
            if p in parentheses: 
                stack.append(p)
            # Closed 
            else: 
                if stack == []: 
                    return False

                last_in = stack.pop()
                if parentheses[last_in] != p:
                    return False

        if stack == []:
            return True
        return False


                 

        