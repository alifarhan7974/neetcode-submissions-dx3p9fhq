class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # m = # num of rows 
        # n = # num of cols 
        grid = [[0] * n] * m 
        grid[0][0] = 1 
        print(grid)

        # Make first row 1 
        for i in range(n): 
            grid[0][i] = 1

        # Make first col 1 
        for i in range(m): 
            grid[i][0] = 1 


        for r in range(1, m): 
            for c in range(1, n): 
                print(r, c) 
                grid[r][c] = grid[r - 1][c] + grid[r][c - 1]


        return grid[-1][-1]

