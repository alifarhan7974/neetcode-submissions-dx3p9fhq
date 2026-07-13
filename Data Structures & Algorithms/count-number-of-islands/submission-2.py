class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # Iterate through grid 
        # Find 1, erase island with dfs, increment island 
        rows, cols = len(grid), len(grid[0])
        res = 0 

        # Wipes out all adjecent ones 
        def dfs(r, c): 
            if not (0 <= r < rows and 0 <= c < cols and grid[r][c] == "1"): 
                return  

            grid[r][c] = "0"

            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        for r in range(rows): 
            for c in range(cols): 
                if grid[r][c] == "1": 
                    res += 1 
                    dfs(r, c)


        return res 






            


        