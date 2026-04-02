class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        full = [i for i in range(len(nums)+ 1)]

        full_xor, missing_xor = 0, 0 

        for num in nums: 
            missing_xor ^= num

        for num in full: 
            full_xor ^= num

        return full_xor ^ missing_xor