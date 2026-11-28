"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals.sort(key=lambda x: x.start)
        free_times = []
        
        for interval in intervals:
            if free_times and free_times[0] <= interval.start:
                heapq.heappop(free_times)
            heapq.heappush(free_times, interval.end)

        return len(free_times)