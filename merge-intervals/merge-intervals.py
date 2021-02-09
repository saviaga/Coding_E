class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        res = []
        
        intervals.sort(key=lambda x: x[0])
        res.append(intervals[0])
        for i in range(1,len(intervals)):
            print(res,i)
            if res[-1][1] < intervals[i][0]:
                
                res.append(intervals[i])
            if res[-1][1] >= intervals[i][0]:
                res[-1][1] = max(res[-1][1],intervals[i][1])
            
        return res
        