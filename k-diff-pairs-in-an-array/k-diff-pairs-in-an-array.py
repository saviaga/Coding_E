import numpy as np
class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        
        count = 0
        dict_items = collections.Counter(nums)
        
        for key in dict_items:
            if k > 0 and key+k in dict_items:
                count+=1
            elif k ==0 and dict_items[key] > 1:
                count+=1
        return count
            
        
         
        
        