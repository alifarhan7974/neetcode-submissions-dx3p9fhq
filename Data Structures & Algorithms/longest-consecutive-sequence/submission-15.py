class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Base Case 
        if nums == []: 
            return 0

        seen = set() 
        lookup = set(nums)
        longest = 1

        for num in lookup: 
            # Greedily count if start of sequence 
            if num - 1 not in lookup:         
                count = 1 
                curr = num
                while curr + 1 in lookup:
                    count += 1 
                    curr += 1
                    longest = max(longest, count)

        return longest 



