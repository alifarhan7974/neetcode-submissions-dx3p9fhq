from collections import deque 
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        queue = deque()  
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        mins = 0 
        fresh = 0 


        for r in range(rows): 
            for c in range(cols): 
                if grid[r][c] == 2:
                    queue.append((r, c))
                elif grid[r][c] == 1:
                    fresh += 1 

        # Explore until no fresh fruit 
        while queue and fresh > 0: 
            # Process curr level 
            for _ in range(len(queue)): 
                r, c = queue.popleft()

                # Process neighbors 
                for dr, dc in directions: 
                    nr = r + dr 
                    nc = c + dc 

                    if nr < 0 or nc < 0 or nr >= rows or nc >= cols: 
                        continue
                    
                    if grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        queue.append((nr, nc))
                        fresh -= 1 
            mins += 1 

        return mins if fresh == 0 else -1 

                

        