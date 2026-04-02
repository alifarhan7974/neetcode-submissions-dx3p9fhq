class Solution {
public:
    int findMin(vector<int> &nums) {
        int left = 0; 
        int right = nums.size() - 1; 

        while (left < right) { 
            int middle = (left + right) / 2; 

            if (nums[middle] > nums.back()) { 
                left = middle + 1; 
            }
            else { // nums[middle] <= nums[end] 
                right = middle; 
            }
        }

        return nums[left]; 
        
    }
};
