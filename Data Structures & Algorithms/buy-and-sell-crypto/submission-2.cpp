class Solution {
public:
    int maxProfit(vector<int>& prices) {
        // buy on lowest day 
        // iterate through list as sell day
        int buy = prices[0]; 
        int max_profit = 0; 
        int current_profit;

        // Let i be selling day 
        for (int i = 0; i < prices.size(); i++) { 
            buy = min(buy, prices[i]);
            current_profit = prices[i] - buy;
            //cout << "current_profit: " << current_profit << endl; 
            //cout << "maxprofit: " << max_profit << endl; 
            max_profit = max(max_profit, current_profit);
        }

        return max_profit; 
        
    }
};
