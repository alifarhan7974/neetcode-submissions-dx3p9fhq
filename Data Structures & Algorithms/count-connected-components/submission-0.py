from collections import defaultdict
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        graph = defaultdict(list)
        for u, v in edges: 
            graph[u].append(v)
            graph[v].append(u)

        to_visit = {i for i in range(n)}

        def dfs(node): 
            for nei in graph[node]: 
                if nei in to_visit: 
                    to_visit.remove(nei)
                    dfs(nei) 

        count = 0
        while to_visit: 
            node = to_visit.pop()
            dfs(node)
            count += 1

        return count 