from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows, cols = len(grid), len(grid[0])
        INF = 2**31 - 1 
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]


        queue = deque([]) # (row, col, dist)

        # Append treasures to the queue 
        for r in range(rows): 
            for c in range(cols): 
                if grid[r][c] == 0: 
                    queue.append((r, c))


        # BFS (only holds one that can reach treasure)
        while queue: 
            r, c = queue.popleft()

            for x, y in directions: 
                nr, nc = r + x, c + y

                if not (0 <= nr < rows and 0 <= nc < cols): 
                    continue
                
                if grid[nr][nc] != INF: 
                    continue 

                grid[nr][nc] = grid[r][c] + 1 
                queue.append((nr, nc))
                

        

                
            



        
                    

            

            

            