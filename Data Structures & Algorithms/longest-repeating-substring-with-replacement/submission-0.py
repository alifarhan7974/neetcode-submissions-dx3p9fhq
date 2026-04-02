class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0 
        max_len = 0
        counter = dict()
        most_freq = 0 

        for right in range(len(s)): 
            if s[right] in counter: 
                counter[s[right]] += 1 
            else: 
                counter[s[right]] = 1 

            most_freq = max(most_freq, counter[s[right]])
            window_size = right - left + 1 


            #print(counter) 
            if window_size - most_freq > k: 
                counter[s[left]] -= 1 
                left += 1

            max_len = max(max_len, right - left + 1)
            print(f"max_len: {max_len}")


        return max_len


         
