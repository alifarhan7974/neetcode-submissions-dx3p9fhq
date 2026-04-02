class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        all_nums = set(nums) 
        res, seq = 0, 1

        for num in all_nums: 
            print(f"num: {num}")
            if num - 1 not in all_nums: 
                seq = 1 
                while (num + 1) in all_nums: 
                    seq += 1 
                    num += 1 
            
            res = max(res, seq)


        return res

        





        