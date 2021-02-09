class Solution(object):
    def countGoodRectangles(self, rectangles):
        """
        :type rectangles: List[List[int]]
        :rtype: int
        """
        count = 0
        for i in range(len(rectangles)):
            rectangles[i] = min(rectangles[i][0],rectangles[i][1])
        max_elem = max(rectangles)        
        for elem in rectangles:
            if elem >= max_elem:
                count+=1
        return count
            
        