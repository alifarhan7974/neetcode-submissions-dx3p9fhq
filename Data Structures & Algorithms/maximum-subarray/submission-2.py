class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # dp[i] = maximum sum ending at index i 
        dp = [float('-inf')] * len(nums)
        dp[0] = nums[0]

        for i in range(1, len(nums)): 
            dp[i] = max(
                nums[i] + dp[i - 1], # continue curr subarray
                nums[i], # start new subarray 
            )
        
        return max(dp) 
         



        