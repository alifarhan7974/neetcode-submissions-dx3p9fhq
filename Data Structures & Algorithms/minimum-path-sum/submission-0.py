class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        inf = float('inf')

        dp = [[0] * cols for _ in range(rows)]
        dp[0][0] = grid[0][0]


        for r in range(rows): 
            for c in range(cols): 
                if r == 0 and c == 0: 
                    continue 

                right, down = inf, inf

                if r - 1 >= 0: 
                    right = dp[r - 1][c] 

                if c - 1 >= 0: 
                    down = dp[r][c - 1]

                # cheapest way to get to (r, c) 
                dp[r][c] = grid[r][c] + min(right, down) 

        return dp[-1][-1]


        