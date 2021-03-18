import numpy as np
class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        
        counter = 0
        elements = collections.Counter(nums)
        
        for key,value in elements.items():
            if k > 0 and key+k in elements:
                counter+=1
            elif k ==0 and key+k in elements:
                if elements[key+k] > 1:
                    counter+=1
        return counter
        
         
        
        