class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = [] 
        current  = []

        def backtrack(index): 
            if index == len(nums):
                result.append(current.copy())
                return;

            # Backtrack with current element
            current.append(nums[index])
            backtrack(index + 1)

            # Backtrack without current index 
            current.pop() 
            backtrack(index + 1)

        backtrack(0)
        return result
            
            
            
