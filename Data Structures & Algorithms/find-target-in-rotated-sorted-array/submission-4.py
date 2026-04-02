class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            middle = (left + right) // 2 
            print(f"left: {left}, right: {right}, middle: {middle}") 

            if nums[middle] == target: 
                return middle 

            # Is left half sorted 
            if nums[left] <= nums[middle]: 

                # If target in left side serach left side 
                if nums[left] <= target <= nums[middle]: 
                    right = middle
                    continue
                
                # Search right side 
                else: 
                    left = middle + 1 
                    continue

            # Right side is sorted 
            elif nums[middle] <= nums[right]:  

                # Search right side 
                if nums[middle] <= target <= nums[right]: 
                    left = middle 
                    continue 
                
                # Search for the left side 
                else: 
                    right = middle - 1 
                    continue 
        return - 1 


