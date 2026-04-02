class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start = 0
        middle = len(nums) // 2
        end = len(nums) - 1

        while start <= end: 
            if target < nums[middle]: 
                end = middle - 1
                middle = (start + end) // 2 
            elif nums[middle] < target:
                start = middle + 1
                middle = (start + end) // 2
            else: 
                return middle

        return -1 
        
        