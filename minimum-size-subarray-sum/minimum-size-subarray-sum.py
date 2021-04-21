class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        start = 0
        min_size = float('inf')
        window_sum = 0
        for end in range(len(nums)):
            right_num = nums[end]
            window_sum += right_num
            while window_sum >= target:
                window_size = end-start+1       
                min_size = min(min_size,window_size)
                window_sum -= nums[start]
                start+=1
        if min_size == float('inf'):
            return 0
        return min_size
            
        