from collections import defaultdict
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # Will check in undir graph for cycles 
        # In a tree: edges = num_nodes - 1 
        if len(edges) != n - 1: 
            return False 

        graph = defaultdict(list)
        for u, v in edges: 
            graph[u].append(v)
            graph[v].append(u)

        visited = set()

        def dfs(node): 
            if node in visited:
                return 
            
            visited.add(node)
            for nei in graph[node]: 
                dfs(nei)

        dfs(0)
        return len(visited) == n 



                    
             