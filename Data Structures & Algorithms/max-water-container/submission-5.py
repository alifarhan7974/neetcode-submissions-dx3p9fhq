class Solution:
    def maxArea(self, heights: List[int]) -> int:
        volume = 0
        l, r = 0, len(heights) - 1

        while l < r: 
            curr_vol = (r - l) * min(heights[l], heights[r])
            volume = max(curr_vol, volume)
            if heights[l] < heights[r]: 
                l += 1
            else: 
                r -= 1 

        return volume 