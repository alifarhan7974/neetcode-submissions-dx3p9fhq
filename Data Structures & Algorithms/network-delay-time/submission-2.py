import heapq
from collections import defaultdict

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for u, v, t in times: 
            graph[u].append((v, t))

        heap = [(0, k)] # t, node 
        visited = {}

        while heap: 
            time, node = heapq.heappop(heap)

            if node in visited: 
                continue

            visited[node] = time

            for v, t in graph[node]: 
                if v not in visited: 
                    heapq.heappush(heap, (time + t, v))

        print(visited)
        return max(visited.values()) if len(visited) == n else -1 
        



        
        
       



