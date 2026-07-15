"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if not intervals or len(intervals)<=1:
            return True 
        
        intervals.sort(key=lambda i: i.start)

        for i in range(1,len(intervals)):
            current_meeting = intervals[i]
            previous_meeting = intervals[i-1]


            if current_meeting.start < previous_meeting.end:
                return False 
        
        return True 