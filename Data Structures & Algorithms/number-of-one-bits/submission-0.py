class Solution:
    def hammingWeight(self, n: int) -> int:
        bits = [int(bit) for bit in bin(n)[2:]]
        ones = 0

        for bit in bits: 
            if bit & 1:
                ones += 1

        return ones
