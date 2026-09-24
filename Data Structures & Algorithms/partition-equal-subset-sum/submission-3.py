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
            # Out of bounds -> False
            if i == n or curr > target: 
                return False 

            # In table ret table 
            if dp[i][curr] != None: 
                return dp[i][curr]

            if curr == target: 
                return True 

            # Choose i 
            curr += nums[i] 
            keep = dfs(curr, i + 1)

            # Skip i 
            curr -= nums[i] 
            skip = dfs(curr, i + 1)

            result = keep or skip 
            dp[i][curr] = result 
            return result 

        return dfs(0, 0)


            


                


         
                



        


        