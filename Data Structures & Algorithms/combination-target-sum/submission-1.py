class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = [] 
        n = len(nums)

        def backtrack(i, remaining, combo): 
            #print(f"i: {i}, reamaining: {remaining}, combo: {combo}")

            if remaining == 0: 
                res.append(combo[:])
                return

            if i == n or remaining < 0:
                return

            # Choose i 
            combo.append(nums[i])
            backtrack(i, remaining - nums[i], combo)

            # Skip i 
            combo.pop()
            backtrack(i + 1, remaining, combo)
            

        backtrack(0, target, [])
        return res
            




            
        