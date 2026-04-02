"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        start_times = [time.start for time in sorted(intervals, key=lambda x : x.start)]
        end_times = [time.end for time in sorted(intervals, key = lambda x : x.end)]

        days, count = 0, 0 
        s, e = 0, 0 
        while s < len(start_times): 
            if start_times[s] < end_times[e]:
                count += 1 
                s += 1 
                days = max(days, count)
            else: 
                count -= 1 
                e += 1 

        return days 


