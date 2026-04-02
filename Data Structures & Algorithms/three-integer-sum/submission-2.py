class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # fix one num make it two sum 
        nums.sort()
        res = []

        for i in range(len(nums)): 
            #target = nums[i] + nums[j] + nums[k]
            #target - nums[i] = nums[j] + nums[k]
            if i > 0 and nums[i] == nums[i - 1]: 
                continue 

            complement = 0 - nums[i]
            j = i + 1
            k = len(nums) - 1 

            while j < k: 
                if nums[j] + nums[k] > complement: 
                    k -= 1 

                elif nums[j] + nums[k] < complement: 
                    j += 1
                    
                else: 
                    res.append([nums[i], nums[j], nums[k]])

                    j += 1
                    k -= 1 

                    #skip duplicates 
                    while j < k and nums[j] == nums[j - 1]: 
                        j += 1

                    while j < k and nums[k] == nums[k + 1]: 
                        k -= 1 

        return res 
            
            


        