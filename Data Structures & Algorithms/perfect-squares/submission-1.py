class Solution:
    def numSquares(self, n: int) -> int:
        inf = float('inf')
        dp = [inf] * (n + 1) # dp[i] = min ps to make i 
        dp[1] = 1 
        dp[0] = 0 

        perfect_squares = [x * x for x in range(1, 10000) if x * x <= n] 

        for ps in perfect_squares: 
            for i in range(len(dp)): 
                if i - ps >= 0: 
                    dp[i] = min(1 + dp[i - ps], dp[i])

        return dp[n]  