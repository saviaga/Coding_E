class Solution:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:
        nums.sort()
        l=0
        r = len(nums)-1
        max_sum = -1
        while l < r:
            current_sum = nums[l]+nums[r]
            if current_sum >= k:
                r-=1
            else:
                max_sum = max(max_sum,current_sum)
                l+=1
        return max_sum
                
                
        
        
        
        
        
        
        
        
        
        
        
        