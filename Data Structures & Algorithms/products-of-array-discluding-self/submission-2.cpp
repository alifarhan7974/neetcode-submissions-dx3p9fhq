class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        int length = nums.size();
        vector<int> prefix = vector<int>(length, 1);
        vector<int> suffix = vector<int>(length, 1);


        for (int i = 1; i < length; i++) { 
            prefix[i] = prefix[i-1] * nums[i-1];
        } 

        for (int i = length-2; i >= 0; i--) { 
            suffix[i] = suffix[i+1] * nums[i+1];
        }

        vector<int> product = vector<int>(length); 
        for (int i = 0; i < length; i++) { 
            product[i] = prefix[i] * suffix[i]; 
        }

        return product;
    }
};
