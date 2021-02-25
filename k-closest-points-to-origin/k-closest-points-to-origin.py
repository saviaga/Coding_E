class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        x1,y1= 0,0
        distances = DefaultDict(list)
        #X2
        res =[]
        for i in range(len(points)):
            x2 = points[i][0]
            y2 = points[i][1]
            e_distance = sqrt((x1-x2)**2 + (y1-y2)**2)
            distances[i] = e_distance
        for key, dist in sorted(distances.items(),key=lambda x:x[1]):
            res.append(points[key])
        
        return res[:K]           
        
        
            
            
        