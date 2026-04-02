class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        highest_profit = 0 
        buy = prices[0]

        for sell in prices: 
            buy = min(buy, sell) 
            curr_profit = sell - buy 
            highest_profit = max(highest_profit, curr_profit)

        return highest_profit 
            




        

            