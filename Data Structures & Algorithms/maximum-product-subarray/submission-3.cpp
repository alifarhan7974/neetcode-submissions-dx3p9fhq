class Solution {
public:
    int maxProduct(vector<int>& nums) {
        int curr_max = nums[0];
        int curr_min = nums[0];
        int res = nums[0]; 

        for (int i = 1; i < nums.size(); i++) { 
            int prev_min = curr_min; 
            int prev_max = curr_max; 

            curr_max = max({
                nums[i] * prev_min,
                nums[i] * prev_max, 
                nums[i]
            });
            curr_min = min({
                nums[i] * prev_min,
                nums[i] * prev_max, 
                nums[i]
            });
            res = max(res, curr_max); 
        }

        return res; 
    }
};
