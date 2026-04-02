class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1: 
            return nums[0]
        if len(nums) == 2: 
            return max(nums)
        
        def helper(nums):
            if len(nums) == 1: 
                return nums[0]
    
            rob1 = nums[0]
            rob2 = max(nums[0], nums[1])

            for i in range(2, len(nums)): 
                curr = max(nums[i] + rob1, rob2)
                rob1 = rob2
                rob2 = curr
    
            return rob2 

        return max(helper(nums[1:]), helper(nums[:-1]))
    
            


        