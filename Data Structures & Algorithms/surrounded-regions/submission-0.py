class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows, cols = len(board), len(board[0])
        grid = board 

        def dfs(r, c): 
            if not (0 <= r < rows and 0 <= c < cols and grid[r][c] == "O"): 
                return 

            grid[r][c] = "S" 
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        for r in range(rows): 
            for c in range(cols): 
                if ((r == 0 or r == rows - 1) or (c == 0 or c == cols - 1)) and grid[r][c] == "O":  
                    dfs(r, c)



        for r in range(rows): 
            for c in range(cols): 
                if grid[r][c] == "O": # Not safe flip to X  
                    grid[r][c] = "X" 
                if grid[r][c] == "S": # Safe flip back to O  
                    grid[r][c] = "O"

        

            
                
                 

            




            

            

        