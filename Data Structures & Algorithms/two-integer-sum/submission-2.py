class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        complements = dict() # Key=target-num, val=index

        for i, val in enumerate(nums):
            difference = target - val
            if difference in complements:
                return [complements[difference], i]
            complements[val] = i

        #print(complements)
        return []

        