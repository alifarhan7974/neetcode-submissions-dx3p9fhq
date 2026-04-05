class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # Iterate through grid 
        # Find 1, erase island with dfs, increment island 

        if not grid: 
            return 0

        rows, cols = len(grid), len(grid[0])
        islands = 0 

        def dfs(r, c): 
            # Break if encounter a 1 or out of bounds 
            if r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] == "0": 
                return 

            grid[r][c] = "0" # So future dfs calls will break here 

            dfs(r, c + 1) # right 
            dfs(r, c - 1) # left 
            dfs(r + 1, c) # up
            dfs(r - 1, c) # down


        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    islands += 1 
                    dfs(r, c)

        return islands 

        