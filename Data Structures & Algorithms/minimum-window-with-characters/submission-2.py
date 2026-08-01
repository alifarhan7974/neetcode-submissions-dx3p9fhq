from collections import Counter, defaultdict

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s): 
            return ""
        


        l, r = 0, 0 
        best_len = float('inf')

        need = Counter(t)  # Counter of t 
        window = defaultdict(int)  # curr window 

        required = len(need) # Number of unique characters 
        formed = 0 # number of characters that match 

        left = 0 
        for right in range(len(s)): 
            # Expand window 
            print(window, need)

            if s[right] in need: 
                window[s[right]] += 1 

                if window[s[right]] == need[s[right]]: 
                    formed += 1 

                while formed == required: 
                    if right - left + 1 < best_len: 
                        l, r = left, right
                        best_len = right - left + 1 

                    if s[left] in window: 
                        window[s[left]] -= 1 

                        if window[s[left]] + 1 ==  need[s[left]]: 
                            formed -= 1 


                    left += 1 


        return s[l:r+1] if best_len != float('inf') else ""






            
            
        


            

        

        
    
            
        
       
        




       

