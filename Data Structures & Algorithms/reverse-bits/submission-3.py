class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        for _ in range(32):    
            res = res << 1 
            res = res | (1 & n)
            #print(f"Filled lsb res: {res:032b}")
            #print(f"Shifted itleft: {res:032b}")
            n = n >> 1 
    
        
        #print(f"Final res: {res:032b}")
        #print(f"Expected:  10101000000000000000000000000000")

        return res 