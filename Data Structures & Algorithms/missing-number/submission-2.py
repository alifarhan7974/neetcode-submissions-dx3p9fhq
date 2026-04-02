class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        all_nums = 0
        incomplete_nums = 0

        for i in range(len(nums)+1):
            all_nums = all_nums ^ i
        
        for num in nums: 
            incomplete_nums ^= num

        return all_nums ^ incomplete_nums
