class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        cs = 0
        count =0 
        dict_sum = {0:1}
        for elem in nums:
            cs +=elem
            if cs - k in dict_sum:
                count+=dict_sum[cs-k]
            
            if cs in dict_sum:
                dict_sum[cs]+=1
            else:
                dict_sum[cs]=1
        return count
                    
        