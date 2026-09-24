class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)

        if total % 2: 
            return False 

        target = total // 2 
            
        n = len(nums)
        
        memo = {}  
        def dfs(curr, i): 
            if (curr, i) in memo: 
                return memo[(curr, i)] 

            if i == n or curr > target: 
                memo[(curr, i)] = False 
                return False 

            if curr == target: 
                return True 

            # Choose i 
            curr += nums[i] 
            keep = dfs(curr, i + 1)

            # Skip i 
            curr -= nums[i] 
            skip = dfs(curr, i + 1)

            memo[(curr, i)] = keep or skip 
            return memo[(curr, i)]

        return dfs(0, 0)


            


                


         
                



        


        