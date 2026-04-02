
class Solution { 
    public: 
        int maxArea(vector<int>& heights) { 
            int i = 0;
            int j = heights.size()-1; 
            int volume = 0; 

            while (i < j) { 
                int current_volume = (j - i) * min(heights[i], heights[j]);                 
                volume = max(current_volume, volume); 

                heights[i] < heights[j] ? i++ : j--; 
            } 

            return volume;
        } 
};
