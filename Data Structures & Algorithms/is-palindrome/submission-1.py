class Solution:
    def isPalindrome(self, s: str) -> bool:
        alphabet = "abcdefghiklmnopqrstuvwxyz1234567890"
        start, end = 0, len(s) -1
        while start < end: 
            if s[start].lower() == " " or s[start].lower() not in alphabet:
                start += 1
                continue
            if s[end].lower() == " " or s[end].lower() not in alphabet:
                end -= 1
                continue

            if s[start].lower() != s[end].lower():
                return False
            
            start += 1
            end -= 1
            
        return True


        return True