class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        
        count = 0
        cs = 0
        dict_sum = {}
        
        for i in range(len(nums)):
           
            cs += nums[i];
            if cs == k:
                count+=1
            if (cs - k) in dict_sum: 
                count += dict_sum[cs - k]
            
            if cs in dict_sum:
                dict_sum[cs]+=1
            else:
                dict_sum[cs]=1
       
        return count
            
            
                