class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if len(points)==0:
            return 0
        st = 1
        points.sort(key = lambda x:x[1])
        prev_end = points[0][1]
        arrow = 1
        
        while st<len(points):
            if prev_end < points[st][0]:
                arrow+=1
                prev_end = points[st][1]
            st+=1
        return arrow
            
        