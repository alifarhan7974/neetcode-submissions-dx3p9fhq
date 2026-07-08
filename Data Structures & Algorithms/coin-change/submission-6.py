class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # since coin value cant be less than 1 
        dp = [amount + 1] * (amount + 1) # dp[i] = min coins to make i dollars 
        dp[0] = 0

        for i in range(len(dp)): 
            for coin in coins: 
                if i - coin >= 0: 
                    dp[i] = min(1 + dp[i - coin], dp[i])


        print(dp )

        return dp[amount] if dp[amount] != amount + 1 else -1 

        