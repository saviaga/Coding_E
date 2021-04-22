class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        
        start = 0
        max_avg_value = float('-inf')
        window_size = 0
        window_sum = 0
        
        for end in range(len(nums)):
            nums_right = nums[end]
            window_sum += nums_right
            
            if end >= k -1:
                max_avg_value = max(max_avg_value,window_sum/k)
                window_sum-=nums[start]
                start+=1
        return max_avg_value
        