class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        if len(nums)<=1: return False
        dict_elems = {}
        cs = 0
        for i in range(len(nums)):
           
            cs+=nums[i]  
            if k!=0:
                cs = cs%k        
             #   print(cs,"-i",i,dict_elems)
            if cs == 0 and i>0: return True
            
            if cs in dict_elems:
                
                if i - dict_elems[cs] > 1:
                    return True                
            else:
                dict_elems[cs] = i
       # print(dict_elems)
        return False
                
            
            
    
    
        
                