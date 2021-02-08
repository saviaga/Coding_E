class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
               
        intervals.sort(key=lambda x: x[0])
        res = [] 
        
        for interval in intervals:
            # if the list of res is empty or if the current
            # interval does not overlap with the previous, simply append it.
            if not res:
                res.append(interval)
            if res[-1][1]<interval[0]:
                res.append(interval)
            else:
                # otherwise, there is overlap, so we merge the current and previous intervals.
                res[-1][1] = max(interval[1],res[-1][1])
        return res
                
            
            
                