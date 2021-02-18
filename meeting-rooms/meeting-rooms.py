class Solution(object):
    def canAttendMeetings(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: bool
        """
        if not intervals:
            return True
        
        intervals.sort()
        first_meeting_end = intervals[0][1]
        
        for elem in intervals[1:]:
            
            next_meeting_start = elem[0]
            if first_meeting_end > next_meeting_start:
                return False
            else:
                first_meeting_end = elem[1]
        return True
            
            
        