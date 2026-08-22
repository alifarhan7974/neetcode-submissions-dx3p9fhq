class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1

        while True: 
            if nums[l] == nums[r]: 
                return nums[l]

            mid = (l + r) // 2 

            # Minimum must be to right of mid 
            if nums[mid] > nums[r]: 
                l = mid + 1   

            # Min could be mid or to the left 
            elif nums[mid] <= nums[r]: 
                r = mid 


        return -1 

            
            







                

           
        