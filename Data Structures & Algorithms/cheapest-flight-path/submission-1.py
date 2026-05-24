from collections import defaultdict
import heapq
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # initialize graph 
        graph = defaultdict(list)

        for origin, dest, price in flights: 
            graph[origin].append((dest, price))

        heap = [(0, 0, src)] # price, stops, node

        while heap: 
            p, s, node = heapq.heappop(heap)

            # Only check if we reach dst, we check stops when pushing
            if node == dst: 
                return p

            if s > k: 
                continue 
                 
            for nei, price in graph[node]: 
                heapq.heappush(heap, (p + price, s + 1, nei))

        return -1 

            





        