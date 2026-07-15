from collections import deque 
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        queue = deque([])

        # Enquee all rotten fruit 
        fresh_fruit = 0 
        for r in range(rows): 
            for c in range(cols): 
                if grid[r][c] == 2: 
                    queue.append((r, c))
                if grid[r][c] == 1: 
                    fresh_fruit += 1 

        mins = 0 
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        while queue and fresh_fruit > 0: 
            n = len(queue)
            for _ in range(n): 
                r, c = queue.popleft()

                # Explore neighbors of rotten fruit 
                for dr, dc in directions: 
                    new_r = r + dr
                    new_c = c + dc 

                    # Enque rotten fruit 
                    if 0 <= new_r < rows and 0 <= new_c < cols and grid[new_r][new_c] == 1:
                        queue.append((new_r, new_c))
                        grid[new_r][new_c] = 2 
                        fresh_fruit -= 1 

            mins += 1 


        return mins if fresh_fruit == 0 else -1 










        

                

        