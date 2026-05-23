"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
    
        intervals = sorted(intervals, key=lambda x: x.start)

        rooms = []

        for meeting in intervals:
            if rooms:
                if rooms[0] <= meeting.start:
                    heapq.heappop(rooms)
                    heapq.heappush(rooms, meeting.end)
                else:
                    heapq.heappush(rooms, meeting.end)
            else:
                heapq.heappush(rooms, meeting.end)

        return len(rooms)


        
        