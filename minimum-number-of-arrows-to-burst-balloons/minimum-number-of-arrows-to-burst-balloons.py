class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if not points:
            return 0
        
        points.sort(key = lambda x:x[1])
        
        first_end = points[0][1]
        num_arrows = 1
        for start,end in points[1:]:
           
            #if balloon starts after first end
            if start > first_end:
                num_arrows+=1
                first_end = end
        return num_arrows
                
            
        
        