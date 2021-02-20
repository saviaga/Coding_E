class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        dict_comp = {0:1}
        total_sum = 0
        count=0
        
        for elem in nums:
            total_sum+=elem
            complement = total_sum - k
            if complement in dict_comp:
                count+= dict_comp[complement]
            
            if total_sum in dict_comp:
                dict_comp[total_sum]+=1
            else:
                dict_comp[total_sum]=1
       
        return count
                
            
            
        