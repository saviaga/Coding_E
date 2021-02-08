class Solution(object):
    def canAttendMeetings(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: bool
        """
        intervals.sort(key=lambda intervals:intervals[0])
        for i in range(len(intervals)-1):
            if intervals[i][1]> intervals[i+1][0]:
                return False
        return True
            
            
        
        
        