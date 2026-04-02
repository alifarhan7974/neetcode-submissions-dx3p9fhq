class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1] * len(nums) 
        for i in range(1, len(nums)):
            prefix[i] = prefix[i-1] * nums[i-1]

        suffix = [1] * (len(nums))
        for i in range(len(nums)-2, -1, -1):
            suffix[i] = suffix[i+1] * nums[i+1]

        print(prefix)
        print(suffix)

        return [x * y for x, y in zip(prefix, suffix)]

        return []