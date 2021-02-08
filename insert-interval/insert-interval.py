class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        
        res = []
        intervals.append(newInterval)
        intervals.sort(key=lambda x: x[0])
        for interval in intervals:
            #if res is empty or no overlapping just add
            if  not res or res[-1][1] < interval[0]:
               
                res.append(interval)
            else:
            #merge
                res[-1][1] = max(res[-1][1],interval[1])
        return res
            
        