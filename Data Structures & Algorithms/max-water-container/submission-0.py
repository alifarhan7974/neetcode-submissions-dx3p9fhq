class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i = 0
        j = len(heights) - 1 
        volume = 0  

        while (i < j): 
            current_volume = (j - i) * min(heights[i], heights[j])
            volume = max(volume, current_volume)

            if (heights[i] < heights[j]):
                i += 1
            else: 
                j -= 1

        return volume 


        


