class Solution {
public:
    int missingNumber(vector<int>& nums) {
        int xor_all = 0; 
        int xor_nums = 0; 

        for (int i = 0; i < nums.size()+1; ++i) { 
            xor_all ^= i;
        }
        
        for (int num : nums) { 
            xor_nums ^= num; 
        }

        return xor_all ^ xor_nums; 
    }
};
