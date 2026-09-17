class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [] 
        n = len(heights)
        heights.append(0)
        max_area = 0 

        for i, height in enumerate(heights): 
            while stack and heights[stack[-1]] > height: 
                prev = stack.pop()
                h = heights[prev]

                if stack: 
                    # right boundry - rectangle - left boundry 
                    width = i - stack[-1] - 1 
                else: 
                    width = i 

                max_area = max(max_area, h * width)

            stack.append(i)

        return max_area 









