class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        res,sumk = 0,0
        #sum first k elements
        for i in range(k): 
            sumk+=nums[i]
        res = sumk
        #sum right next elemnt rest left elem     
        for i in range(k,len(nums)):
            sumk+= nums[i] - nums[i-k]
            res = max(res,sumk)
        return res/k
        