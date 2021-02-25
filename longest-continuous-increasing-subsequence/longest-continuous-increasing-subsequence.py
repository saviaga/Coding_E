class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
       
        size = 1
        longest = 1
        for i in range(1, len(nums)):
            if nums[i-1] < nums[i]:
                size+=1
            else:
                size=1
            
            longest = max(longest,size)
        
        return longest
        