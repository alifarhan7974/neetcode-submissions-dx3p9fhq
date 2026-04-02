class Solution {
public:
    int missingNumber(vector<int>& nums) {
        vector<int> complete(nums.size() + 1);    
        iota(complete.begin(), complete.end(), 0); 

        int complete_xor = 0; 
        int missing_xor = 0; 

        for (int num : complete) { 
            complete_xor ^= num; 
        }

        for (int num : nums) { 
            missing_xor ^= num; 
        }

        return complete_xor ^ missing_xor; 
    }
};
