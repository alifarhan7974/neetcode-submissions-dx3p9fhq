import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [-stone for stone in stones] 
        heapq.heapify(heap)

        while len(heap) >= 2: 
            x, y = heapq.heappop(heap), heapq.heappop(heap)

            if x != y: 
                new_stone = abs(x - y)
                heapq.heappush(heap, -new_stone)

        return -heap[0] if heap else 0 

         
        
        