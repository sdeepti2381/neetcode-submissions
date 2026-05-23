"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if len(intervals) <= 1:
            return True

        intervals = sorted(intervals, key=lambda x: x.start)

        
        start_1, end_1 = intervals[0].start, intervals[0].end
        for i in range(1, len(intervals)):
            start_2, end_2 = intervals[i].start, intervals[i].end
            if start_2 < end_1 and end_2 > start_1:
                return False
            start_1, end_1 = start_2, end_2
        
        return True
            
    

