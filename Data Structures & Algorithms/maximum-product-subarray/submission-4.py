class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        min_array = [0] * n
        max_array = [0] * n
        max_product = [0] * n # Largest subarray up until i 

        min_array[0] = max_array[0] = max_product[0] = nums[0]

        for i in range(1, n): 
            min_array[i] = min(
                min_array[i - 1] * nums[i], 
                max_array[i - 1] * nums[i], 
                nums[i]
            )

            max_array[i] = max(
                min_array[i - 1] * nums[i], 
                max_array[i - 1] * nums[i], 
                nums[i]
            )
        
        return max(max_array)
      

        