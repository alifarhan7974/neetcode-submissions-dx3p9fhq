class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int max_profit = 0; 
        int buy_price = prices[0]; 

        for (int sell_price : prices) {
            int buy_price = min(buy_price, sell_price); 
            int curr_profit = sell_price - buy_price; 

            max_profit = max(curr_profit, max_profit); 
            
        }
        return max_profit; 


    }
};
