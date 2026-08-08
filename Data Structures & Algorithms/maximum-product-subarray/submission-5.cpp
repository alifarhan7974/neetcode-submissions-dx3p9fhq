class Solution {
public:
    int maxProduct(vector<int>& nums) {
        int curr_min = nums[0];
        int curr_max = nums[0]; 
        int res = nums[0]; 

        for (int i = 1; i < nums.size(); i++) { 
            int temp_min  = min({
                curr_min * nums[i], 
                curr_max * nums[i], 
                nums[i]
            });

            int temp_max = max({
                curr_min * nums[i], 
                curr_max * nums[i], 
                nums[i]
            });

            curr_min = temp_min;
            curr_max = temp_max; 

            res = max(res, curr_max); 
        }

        return res; 
    }
};
