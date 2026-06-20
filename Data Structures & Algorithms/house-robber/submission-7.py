class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 2: 
            return max(nums)

        dp = [0] * len(nums)
        dp[0], dp[1] = nums[0], max(nums[0], nums[1]) 

        i = 2
        while i < len(nums): 
            # Rob curr house 
            if nums[i] + dp[i-2] > dp[i-1]:
                dp[i] = nums[i] + dp[i-2]
            else: 
                dp[i] = dp[i-1]

            i += 1 

        print(dp) 
        return max(dp[-1], dp[-2]) 







            
        