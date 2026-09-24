class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)

        # Can only / by 2 if even 
        if total % 2: 
            return False 

        target = total // 2 
        n = len(nums)

        dp = [[None] * (target + 1) for _ in range(n)] 
        
        def dfs(curr, i): 
            if curr == target: 
                return True 

            # Out of bounds -> False
            if i == n or curr > target: 
                return False 

            # In table ret table 
            if dp[i][curr] != None: 
                return dp[i][curr]


            keep = dfs(curr + nums[i], i + 1)
            skip = dfs(curr, i + 1)

             
            dp[i][curr] = keep or skip  
            return dp[i][curr]

        return dfs(0, 0)


            


                


         
                



        


        