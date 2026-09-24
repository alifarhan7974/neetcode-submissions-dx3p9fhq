class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)

        # Can only / by 2 if even 
        if total % 2: 
            return False 

        target = total // 2 
        n = len(nums)

        dp = [False] * (target + 1) #Is there a subset that sums to i
        dp[0] = True 

        for num in nums: 
            for i in range(target, 0, -1): 
                if i - num >= 0 and dp[i - num]: 
                    dp[i] = True 


        return dp[target]

            
         


                


         
                



        


        