class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        // Key: num, Value: index 
        unordered_map<int, int> seen; 

        for (int i = 0; i < nums.size(); i++) { 
            int curr = nums[i]; 
            int complement = target - curr; 

            if (seen.find(complement) != seen.end()) { 
                return {seen[complement], i}; 
            }

            seen[curr] = i; 
        }

        return vector<int> {}; 
        
};
}; 
