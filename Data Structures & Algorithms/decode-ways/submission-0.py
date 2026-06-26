class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        # Want to find dp[0]
        dp = [0] * (n + 1) # dp[i] = number of ways to decode str from index i
        dp[n] = 1 # Reached end; can decode whole string 


        for i in range(n - 1, -1, -1): 
            # Check not 0
            if int(s[i:i+1]) != 0: 
                dp[i] += dp[i + 1]
            else: 
                dp[i] = 0

            if i + 2 <= n and 10 <= int(s[i:i+2]) <= 26: 
                dp[i] += dp[i+2]


        return dp[0]
        



         




     