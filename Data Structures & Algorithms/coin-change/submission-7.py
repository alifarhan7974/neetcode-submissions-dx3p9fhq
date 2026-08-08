class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # since coin value cant be less than 1 
        dp = [float('inf')] * (amount + 1)  
        dp[0] = 0 

        for coin in coins: 
            for i in range(amount + 1): # i is current amount of cents to make 
                if i - coin >= 0: 
                    dp[i] = min(dp[i], 1 + dp[i - coin])

        print(dp) 
        return dp[amount] if dp[amount] != float('inf') else -1



