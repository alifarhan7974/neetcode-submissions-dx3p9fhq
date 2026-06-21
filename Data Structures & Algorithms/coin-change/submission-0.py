class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')] * (amount + 1) # dp[i] = min coins to make i dollars 
        dp[0] = 0 

        # Init dp 
        for coin in coins: 
            if coin <= amount: 
                dp[coin] = 1

        for i in range(1, amount + 1): 
            for coin in coins: 
                if i >= coin: 
                    print(f"i: {i}")
                    dp[i] = min(dp[i], dp[i - coin] + 1)

        return dp[amount] if dp[amount] != float('inf') else -1  