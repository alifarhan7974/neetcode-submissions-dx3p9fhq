class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        min_product = [0] * len(nums)
        max_product = [0] * len(nums)
        
        min_product[0] = nums[0]
        max_product[0] = nums[0]
        res = nums[0]

        for i in range(1, len(nums)): 
            # handle max 
            max_product[i] = max(
                nums[i] * max_product[i - 1],
                nums[i] * min_product[i - 1], 
                nums[i]
            ) 
            min_product[i] = min(
                nums[i] * max_product[i - 1],
                nums[i] * min_product[i - 1], 
                nums[i]
            ) 
            res = max(res, max_product[i])

        print(nums)
        print(max_product)
        print(min_product) 
        return res

        """
        [1, -2, 3] 
        [1, 1, 3]
        [1, -2, -6]

        """



        

        