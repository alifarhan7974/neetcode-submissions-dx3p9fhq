class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        int curr_sum = nums[0]; 
        int res = curr_sum; 

        for (int i = 1; i < nums.size(); i++) { 
            curr_sum = max(
                nums[i] + curr_sum, // continue subarray
                nums[i] // new subarray
            );
            res = max(res, curr_sum); 
        }        

        return res; 
    }
};
