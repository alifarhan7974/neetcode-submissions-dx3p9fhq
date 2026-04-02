class Solution:
    def missingNumber(self, nums: List[int]) -> int:
       length = len(nums)

       complete_set = {i for i in range(length+1)}
       nums = set(nums)
       print(f"Complete_set {complete_set}")
       print(f"nums {nums}")
       diff = complete_set - nums
       print(f"diff {diff}")

       diff = list(diff) 
       return diff[0]
    