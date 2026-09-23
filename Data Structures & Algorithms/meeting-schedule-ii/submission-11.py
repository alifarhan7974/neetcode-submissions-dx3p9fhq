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

        rooms = 1 
        intervals.sort(key=lambda x : x.start) # Start time sorted 

        heap = [] # End time  

        for meeting in intervals: 
            start, end = meeting.start, meeting.end

            if not heap: 
                heapq.heappush(heap, end)
            
            # Dont need new room 
            elif start >= heap[0]: 
                heapq.heappush(heap, end)
                heapq.heappop(heap)

            # Overlapping
            else: 
                heapq.heappush(heap, end)
                
            rooms = max(rooms, len(heap))
            #print(heap)
                

        return rooms 






            



         


            
        

             



