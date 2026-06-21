class Solution {
public:
    int rob(vector<int>& nums) {
        if (nums.size() <= 2) { 
            return *max_element(nums.begin(), nums.end());  
        }

        int x = nums[0]; // Max money before y  
        int y = max(x, nums[1]); // Max money before i  

        for (int i = 2; i < nums.size(); i++) { 
            if (nums[i] + x > y) { 
                int z = nums[i] + x; 
                x = y; 
                y = z; 
            } else { 
                x = y; 
                // y remains the same 
            }
        }

        return y; 
    }
};
