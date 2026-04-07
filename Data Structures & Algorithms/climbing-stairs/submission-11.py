class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1: 
            return 1
        if n == 2: 
            return 2 

        x = 1
        y = 2

        for _ in range(3, n + 1): 
            x, y = y, x + y  

        return y 
        

       