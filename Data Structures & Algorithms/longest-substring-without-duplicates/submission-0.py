class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        longest = 0
        seen = set()

        for r in range(len(s)): 
            while s[r] in seen: # If encounter duplicate char
                seen.remove(s[l]) # Remove from left 
                l += 1 
            
            seen.add(s[r])
            longest = max(longest, len(seen))

        return longest
