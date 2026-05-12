class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])
        
        pacific = set() 
        atlantic = set() 

        def dfs(r, c, prev_height, ocean, visited, ): 
            if not (0 <= r < rows and 0 <= c < cols):
                return

            if (r, c) not in visited and heights[r][c] >= prev_height: 
                ocean.add((r, c))
                visited.add((r, c))


                dfs(r - 1, c, heights[r][c], ocean, visited)
                dfs(r + 1, c, heights[r][c], ocean, visited)
                dfs(r, c + 1, heights[r][c], ocean, visited)
                dfs(r, c - 1, heights[r][c], ocean, visited)

        # DFS for atlantic 
        for r in range(rows): 
            for c in range(cols): 
                if r == 0 or c == 0: 
                    dfs(r, c, heights[r][c], pacific, set())

                if r == rows - 1 or c == cols - 1: 
                    dfs(r, c, heights[r][c], atlantic, set())


        both = pacific.intersection(atlantic)
        return [[r, c] for r, c in both]


            

            
            






        