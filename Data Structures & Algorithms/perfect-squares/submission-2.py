class Solution:
    def numSquares(self, n: int) -> int:
        inf = float('inf')
        dp = [inf] * (n + 1) # dp[i] = min ps to make i 
        dp[0] = 0 

        # square up until sqrt of n + 1 
        perfect_squares = [x * x for x in range(1, int((n**0.5) + 1)) if x * x <= n] 

        for ps in perfect_squares: 
            for i in range(len(dp)): 
                dp[i] = min(1 + dp[i - ps], dp[i])

        return dp[n]  