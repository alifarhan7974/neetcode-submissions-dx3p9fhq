class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = "" 
        for word in strs: 
            encoded += str(len(word)) + "#" + word

        return encoded 
        

    def decode(self, s: str) -> List[str]:
        i, j = 0, 0 
        decoded = []
        while j < len(s): 
            if s[j] != "#": 
                j += 1 
            else: 
                size = int(s[i:j])
                decoded.append(s[j+1:j+1+size])
                j += size + 1  
                i = j 
                
        return decoded

