class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        
        count = 0
        cs = 0
        dict_elem = {0:1}
        
        for i in range(len(nums)):
            cs+=nums[i]
            if cs-k in dict_elem:
                count+=dict_elem[cs-k]
            
            if cs in dict_elem:
                dict_elem[cs]+=1
            else:
                dict_elem[cs]=1
        print(dict_elem)
        return count
            
            
                