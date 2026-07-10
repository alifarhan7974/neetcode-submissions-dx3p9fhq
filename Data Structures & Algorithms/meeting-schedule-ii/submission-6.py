"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

import heapq

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals: 
            return 0 
            
        intervals.sort(key=lambda s : s.start) 
        heap = [] 
        heapq.heappush(heap, intervals[0].end)

        for i in range(1, len(intervals)): 
            curr_start = intervals[i].start 
            curr_end = intervals[i].end

            # Meeting starts before earliest room avaialbe 
            if curr_start < heap[0]: 
                heapq.heappush(heap, curr_end)

            # Meeting starts after earlier room done 
            elif curr_start >= heap[0]: 
                heapq.heappop(heap)
                heapq.heappush(heap, curr_end)


        return len(heap) 


             



