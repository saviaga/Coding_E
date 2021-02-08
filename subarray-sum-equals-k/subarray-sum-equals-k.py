class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        d = {0:1}
        count=0
        curr_sum=0
        
        for i in range(len(nums)):
            curr_sum+=nums[i]
            if (curr_sum-k) in d:
                count+=d[curr_sum-k]
            if curr_sum in d: 
                d[curr_sum]+=1
            else:
                d[curr_sum]=1
        return count
    
        
                   
            
          