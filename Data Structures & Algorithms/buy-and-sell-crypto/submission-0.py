class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        buy = prices[0]

        for i in range(len(prices)): 
            buy = min(buy, prices[i])
            profit = prices[i] - buy
            
            if profit > max_profit: 
                max_profit = profit

        return max_profit 
            
            