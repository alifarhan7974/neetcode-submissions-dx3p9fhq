class Solution:
    def maxArea(self, heights: List[int]) -> int:
        volume = 0
        left, right = 0, len(heights) - 1 

        while left < right: 
            curr_volume = min(heights[left], heights[right]) * (right - left) 
            volume = max(volume, curr_volume)

            if heights[left] < heights[right]: 
                left += 1 
            else: 
                right -= 1 

        return volume 