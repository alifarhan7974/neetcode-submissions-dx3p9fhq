class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums) 
        dp = [False] * n # dp[i] = Can we reach end starting from i
        dp[-1] = True 

        for jump_start_index in range(n - 2, -1, -1): 
            for jump_len in range(1, nums[jump_start_index] + 1):
                landing_index = jump_start_index + jump_len
                if landing_index >= n:
                    dp[jump_start_index] = True 
                    break

                elif dp[jump_start_index + jump_len]: 
                    dp[jump_start_index] = True 
                    break 


        print(dp) 
        return dp[0]




        