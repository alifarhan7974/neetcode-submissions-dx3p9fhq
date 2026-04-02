class Solution:
    def countBits(self, n: int) -> List[int]:
        total_ones = []
        for num in range(n+1):
            ones = 0
            for i in range(32):
                if (1 << i) & num:
                    ones += 1

            total_ones.append(ones)

        return total_ones