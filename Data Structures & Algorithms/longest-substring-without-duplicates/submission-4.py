class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == "": 
            return 0

        seen = set() 
        res = 1 
        l, r = 0, 0 

        while r < len(s): 
            # Duplicate case 
            if s[r] in seen: 
                while s[r] in seen: 
                    seen.remove(s[l])
                    l += 1 
            # Unique case 
            else: 
                seen.add(s[r])
                r += 1 
                res = max(res, len(seen))

        return res 
            




                



        
            
