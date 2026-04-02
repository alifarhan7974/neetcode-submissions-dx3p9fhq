class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # Duplicate if len of set not eq to len of list
        return len(set(nums)) != len(nums) 