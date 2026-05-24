from collections import defaultdict
import heapq
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # initialize graph 
        graph = defaultdict(list)
        for origin, dest, price in flights: 
            graph[origin].append((dest, price))

        heap = [(0, 0, src)] # price, stops, node

        """
        My train of throught currently
        Can find dest in under k stops 
        find cheapest path to dest but more than k, then backtrack? how to do that
        """ 
        while heap: 
            p, s, node = heapq.heappop(heap)

            if node == dst: 
                return p
                 
            for nei, price in graph[node]: 
                if s <= k: 
                    heapq.heappush(heap, (p + price, s + 1, nei))

        return -1 

            





        