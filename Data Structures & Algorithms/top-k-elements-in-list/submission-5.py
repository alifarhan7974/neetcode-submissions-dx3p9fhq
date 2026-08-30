import heapq
from collections import Counter 
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqs = Counter(nums)
        heap = [] 
        
        for num, freq in freqs.items(): 
            heapq.heappush(heap, (freq, num))

            if len(heap) > k: 
                heapq.heappop(heap)

        return [num for _, num in heap]
        
        

        
        
        