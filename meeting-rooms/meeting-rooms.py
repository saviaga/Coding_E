class Solution(object):
    def canAttendMeetings(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: bool
        """
        if not intervals:
            return True
        
        intervals.sort(key= lambda x: x[0])
        
        
        for i in range(len(intervals)-1):
            first_end = intervals[i][1]
            next_start = intervals[i+1][0]
            if first_end> next_start:
                return False
        return True
            
        