class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        ans = [0] * len(nums)
        start = 0
        end = len(nums)-1
        pos = end
        while start<=end:
            pow_st = nums[start]**2
            pow_end = nums[end]**2
            
            if pow_st>pow_end:
                ans[pos] = pow_st
                start+=1
            else:
                ans[pos] = pow_end
                end-=1
            pos-=1
        return ans
            
        
        
        
                