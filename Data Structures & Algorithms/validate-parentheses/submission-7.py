class Solution:
    def isValid(self, s: str) -> bool:
        matching_pairs = {
            "{" : "}", 
            "(" : ")", 
            "[" : "]"
        }

        stack = [] 

        for c in s: 
            # Open bracket 
            if c in matching_pairs:
                stack.append(c)
            # Closing bracket
            else:
                # Check if empty
                if len(stack) == 0: 
                    return False
                if matching_pairs[stack.pop()] != c:
                    return False

        return len(stack) == 0


