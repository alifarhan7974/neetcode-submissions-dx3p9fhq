import heapq
from collections import defaultdict

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list) 
        for u, v, t in times: 
            graph[u].append((v, t))

        heap = [(0, k)] # (dist, node)

        distances = {} # nodes w/ finalized shortest distances 

        while heap: 
            d, node = heapq.heappop(heap)

            if node in distances: 
                continue

            distances[node] = d 
            
            for nei, weight in graph[node]: 
                if nei not in distances: 
                    heapq.heappush(heap, (d + weight, nei))


        if len(distances) != n:
            return -1 

        return max(distances.values())  

       



