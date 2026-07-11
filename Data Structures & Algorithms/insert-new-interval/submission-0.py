class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = [] 
        
        for start, end in intervals: 
            # new interval is fully after curr 
            if end < newInterval[0]:
                res.append([start, end])

            # New Interval is fully before curr
            elif newInterval[1] < start:
                res.append(newInterval[:])
                newInterval = [start, end]

            # New Interval is in between curr 
            else: 
                newInterval[0] = min(start, newInterval[0])
                newInterval[1] = max(end, newInterval[1])

        res.append(newInterval) 
        return res 

                


            
            
            
        