from collections import heapq
class Solution:
    def longestPalindrome(self, s: str) -> str:
        # centers = len - 2 
        # start from middle if palindrome is found return 
        res = ""
        longest_word = 0 

        for center in range(len(s)): 
            # Odd centers 
            left, right = center, center 
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1 
                right += 1
            
            if right - left > longest_word: 
                longest_word = right - left 
                res = s[left+1:right]

            # Even centers
            left, right = center, center + 1  
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1 
                right += 1
            
            if right - left > longest_word: 
                longest_word = right - left 
                res = s[left+1:right]


        return res


            

        

        