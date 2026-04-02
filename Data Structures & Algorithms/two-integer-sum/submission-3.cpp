class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        map<int, int> complements; 

        for (int i = 0; i < nums.size(); i++) {
            
            int difference = target - nums[i]; 
            if (complements.count(difference) > 0) { 
                return vector<int> {complements[difference], i};
            }
            
            complements[nums[i]] =  i;

        }

        return vector<int> {};
        
    }
};
