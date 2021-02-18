class Solution:
    def countGoodRectangles(self, rectangles: List[List[int]]) -> int:
        
        maxLen = min(rectangles[0]) #get max leng of first rectangle
        num_rectanges = collections.defaultdict(int)
        num_rectanges[maxLen] = 1
        
        for elem in rectangles[1:]:
            lenght = min(elem)
            if lenght >=maxLen:
                maxLen = lenght
                num_rectanges[maxLen]+=1
        return num_rectanges[maxLen]
                
        
        
        