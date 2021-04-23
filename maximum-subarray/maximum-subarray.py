class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
         #edge cases
        max_current = nums[0]
        max_global = nums[0]
       
        for i in range(1,len(nums)):
           
            max_current = max(nums[i],max_current+nums[i])
            max_global = max(max_global,max_current)
            
            
              
        return max_global
        