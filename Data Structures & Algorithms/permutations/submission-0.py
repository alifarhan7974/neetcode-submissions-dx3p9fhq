class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        permutations = [] 
        if len(nums) == 0: 
            permutations.append([])

        for i, v in enumerate(nums):
            remainder = nums[:i] + nums[i+1:]
            perms = self.permute(remainder)
            for perm in perms:
                permutations.append([v] + perm)
                

        return permutations 
