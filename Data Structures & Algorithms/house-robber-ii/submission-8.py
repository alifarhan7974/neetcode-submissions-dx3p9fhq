class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 2: 
            return max(nums) 

        def helper(nums): 
            if len(nums) <= 2: 
                return max(nums)

            x = nums[0]
            y = max(x, nums[1]) 

            for i in range(2, len(nums)): 
                if nums[i] + x > y: 
                    # y = nums[i] + x
                    # x = y 
                    x, y = y, nums[i] + x  
                else: 
                    # x becomes y, y stays the same 
                    x = y 


            return y

        return max(helper(nums[1:]), helper(nums[:-1]))
        