class Solution {
public:
    int minCostClimbingStairs(vector<int>& cost) {
        if (cost.size() <= 2) { 
            return min(cost[0], cost[1]); 
        }

        int x = 0; // cost needed to reach i - 2 
        int y = 0; // cost needed to read i - 1

        for (int i = 2; i <= cost.size(); i++) { 
            int new_y = min(
                x + cost[i - 2],
                y + cost[i - 1]
            );
            x = y; 
            y = new_y; 
        }

        cout << "x " << x << endl; 
        cout << "y " << y << endl; 
        return y; 
    }
};
