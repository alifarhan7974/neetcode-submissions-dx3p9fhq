class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        def helper(nums): 
            if nums == []: 
                yield [] 

            for i, val in enumerate(nums): 
                remainder = nums[:i] + nums[i+1:]
                for perm in helper(remainder): 
                    yield [val] + perm

        return [p for p in helper(nums)] 

        