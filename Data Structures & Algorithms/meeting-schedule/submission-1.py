"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key=lambda x : x.start)

        for i in range(len(intervals) - 1):
            end_first = intervals[i].end
            start_second = intervals[i+1].start

            if start_second < end_first: 
                return False 


        return True 
            


            




        


        


           

        