class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        unordered_set<int> numsSet(nums.begin(), nums.end()); 
        int res = 0; 
        for (int num : numsSet) { 
            if (numsSet.find(num - 1) == numsSet.end()) { 
                int seq = 1; 
                while (numsSet.find(num + seq) != numsSet.end()) { 
                    seq++; 
                }

                res = max(res, seq);
            }
        }

        return res; 
        
    }
};
