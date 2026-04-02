class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if nums == []: 
            return 0
        res = 1
        lookup = set(nums)

        for num in nums: 
            if num + 1 in lookup: 
                count = 1
                while num + count in lookup: 
                    count += 1 
                res = max(res, count) 

        return res



        