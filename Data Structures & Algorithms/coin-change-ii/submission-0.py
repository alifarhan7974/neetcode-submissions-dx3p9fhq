class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0] * (amount + 1) # dp[i] = num ways to make i dollars 
        dp[0] = 1  # 1 way to make 0 dollars 

        for coin in coins: 
            for i in range(len(dp)):
                if i - coin >= 0:
                    dp[i] += dp[i - coin]

        print(dp)
        return dp[amount]


            
        a