class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # target = nums[i] + nums[j], diff = nums[j] = target - nums[i]
        differences_map = {}
        for i in range(0, len(nums)):
            if nums[i] in differences_map:
                return [differences_map[nums[i]], i]
            
            difference = target - nums[i] #current number difference
            differences_map[difference] = i