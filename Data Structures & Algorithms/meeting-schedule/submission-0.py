"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        for i in range(len(intervals)):
            for j in range(i + 1, len(intervals)): 
                start, end = intervals[i].start, intervals[i].end
                start_2, end_2 = intervals[j].start, intervals[j].end

                print(f"start: {start}, end: {end}, start_2: {start_2}, end_2: {end_2}")
                valid_1 = start <= end <= start_2 <= end_2 
                valid_2 = start_2 <= end_2 <= start <= end 
                if valid_1 or valid_2:
                    continue

                return False

        return True
                


        


        


           

        