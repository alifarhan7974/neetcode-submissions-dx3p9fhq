class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        prefix = [1] * len(nums)
        prefix_total = nums[0] 
        for i in range(1, len(nums)): 
            prefix[i] = prefix_total
            prefix_total *= nums[i]

        suffix = [1] * len(nums)
        suffix_total = nums[-1]
        for i in range(len(nums)-2, -1, -1): 
            suffix[i] = suffix_total
            suffix_total *= nums[i]

        #print(f"prefix: {prefix}")
        #print(f"suffix: {suffix}")

        return [p * s for p, s in zip(prefix, suffix)]


            
