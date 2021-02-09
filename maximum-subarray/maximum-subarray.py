class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)==1:
            return nums[0]
        
        run_sum = [nums[0]]
        
        for i in range(1,len(nums)):
            run_sum.append(max(nums[i],run_sum[i-1]+nums[i]))
                      
        return max(run_sum)
        