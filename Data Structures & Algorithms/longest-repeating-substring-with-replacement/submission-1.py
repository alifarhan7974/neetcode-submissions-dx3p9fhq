from collections import defaultdict 
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        window = set() 
        res = 0
        window = defaultdict(int)
        most_freq_letter = 0 
        l = 0 

        for r in range(len(s)): 
            print(window, r, l)
            window[s[r]] += 1 
            most_freq_letter = max(most_freq_letter, window[s[r]])
            while (r - l + 1) - most_freq_letter > k: 
                window[s[l]] -= 1
                l += 1
                most_freq_letter = max(most_freq_letter, window[s[l]])
            res = max(res, r - l + 1)


        return res 

                






            
            




        
